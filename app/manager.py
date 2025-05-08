import asyncio
from asyncio import Future
from enum import Enum
from pathlib import Path
from types import MappingProxyType
from typing import List, Tuple, TypedDict, overload, Callable, Any, Dict, NamedTuple

from requests import Session
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser, JsonParser
from xsdata.formats.dataclass.parsers.config import ParserConfig

from app.scheme.org.eidr.schema.resolution_set_type import KernelMetadata
from app.scheme.org.eidr.schema import RegistrantType, PartyDoilistType, PartyIdlist, QueryResultsType, FullMetadata, \
    SelfDefinedMetadata, InheritedMetadata, SimpleMetadata, ProvenanceMetadata, AlternateIds, LinkedAlternateIds
from app.services import RegistryRequest, ServiceBase, ResponseReader, Query, StatusRequest, Delete
from app.driver import API_Driver, ResolveUserMode, ACL_Type, ModifyType, ResolveRecordMode, ResolvePartyMode, QueryMode
from app.services.eidr_request import RegistryRequestSingle
from app.services.metadata import BaseObjectMeta, FullMeta, ServiceMeta, PartyMeta
from app.services.party_query import PartyQuery
from app.services.registration.interface import RegistrationService
from app.services.service_query import NoOperationRequest, ServiceQuery
from app.services.simple_metadata import SimpleMetadata as SimpleWrapper
from app.services.response_reader import ResponseType
from app.scheme.org.eidr.schema.base_object_info_type import BaseObjectInfoType
from app.config.config import CONFIG_PATH
from app.util import instance_to_dict, repr_non_serials
from app import ConfigDict
import json


class AdminResponseError(Exception):
    ...


def check_err(res: ResponseReader):
    if res.admin_response:
        raise AdminResponseError("\n\nAdmin Response Code {}: {}\n\t{}".format(*res.status, res.get_field("details")))


parser = XmlParser(config=ParserConfig(), context=XmlContext())
json_parser = JsonParser(config=ParserConfig(), context=XmlContext())  # TODO: See if this needed in manager


# Status helpers

def crash_on_status(code: int, details: str) -> None:
    """
    A default handler for status codes that raises an exception.
    :param code:
    :param details:
    """
    raise RuntimeError(f"Got bad status {code}: {details}")


# Default responses for status codes (right now just accept 0)
default_responses = MappingProxyType({  # MappingProxyType is a read-only view of the dict
    0: lambda code, details: "Success"
})


class DuplicateDict(TypedDict):
    id: str
    details: str | None
    score: str | None
    low_threshold: str | None
    high_threshold: str | None


class StatusResult(TypedDict):
    """
    A dictionary to hold the status of an operation. Holds the token, status code, and details.
    The key "extra" is where user-provided status handlers return into.
    """
    token: str
    status: Tuple[int, str]
    details: Tuple[int, str]
    extra: Any
    id: str | None
    dupes: List[DuplicateDict] | None


class BatchStatusResult(TypedDict):
    """
    A dictionary to hold the status of a batch operation. Holds the token, status code, details, and extra information.
    The key "extra" is where user-provided status handlers return into.
    """
    token: str | None
    status: Tuple[int, int]
    details: str
    extra: Any


# ______


def handle_batch_results(res: ResponseReader,
                         status_handlers: Dict[int, Callable[[int, str], Any]] | None = default_responses,
                         default_handler: Callable[[int, str], Any] | None = None) -> List[BatchStatusResult]:
    if not res.has_field("request_status_results"):
        raise ValueError("Response does not contain status results")

    status_res = res.get_field("request_status_results")

    # "status" below is used to get the token in the case of a batch operation
    status = None if not res.has_field("request_status") else res.get_field("request_status")
    results = []
    batch_res = status_res.batch_status
    if batch_res:
        code = batch_res.code.value
        stats = {
            "token": "" if not status else status.token,
            "status": (code, batch_res.type_value.value),
            "details": batch_res.details,
            "extra": None,
        }

        if status_handlers and code in status_handlers:
            stats["extra"] = status_handlers[code](code, batch_res.details)
        elif default_handler:
            stats["extra"] = default_handler(code, batch_res.details)
        results.append(stats)
    return results


def handle_status_results(res: ResponseReader,
                          status_handlers: Dict[int, Callable[[int, str], Any]] | None = default_responses,
                          default_handler: Callable[[int, str], Any] | None = crash_on_status) -> List[StatusResult]:
    """
    Handle the status results from a response.
    :param res: The wrapped response from post()
    :param status_handlers: A dictionary mapping status codes to response handlers (int, str) -> Any. Returned value stored in key "extra". Can be None to default on all status codes.
    :param default_handler: The default handler for status codes not in the status_handlers. Defaults to crashing on unhandled status. Can be None to ignore unhandled status codes.
    :param batch_status_handlers: Identical to status_handlers, but for batch operations. If there are no batch results in res, this will be ignored.
    :param default_batch_handler: Identical to default_handler, but for batch operations. If there are no batch results in res, this will also be ignored.
    :return: A list of dictionaries containing the status of each operation.
    """

    if not res.has_field("request_status_results"):
        raise ValueError("Response does not contain status results")

    status_res = res.get_field("request_status_results")

    results = []

    for op_res in status_res.operation_status:
        code = op_res.status.code.value
        stats = {
            "token": op_res.token,
            "status": (code, op_res.status.type_value.value),
            "details": (op_res.status.details_code, op_res.status.details),
            "extra": None,
            "id": None if not op_res.id else op_res.id.value,
            "dupes": None if not hasattr(op_res, "duplicate") else [
                {
                    "id": dup.id.value,
                    "details": dup.details,
                    "score": dup.score,
                    "low_threshold": dup.low_threshold,
                    "high_threshold": dup.high_threshold
                } for dup in op_res.duplicate
            ]

        }

        if status_handlers and code in status_handlers:
            stats["extra"] = status_handlers[code](op_res.status.code.value, op_res.status.details)
        elif default_handler:
            stats["extra"] = default_handler(op_res.status.code.value, op_res.status.details)
        results.append(stats)

    return results


class RegisterResult(NamedTuple):
    """
    A named tuple to hold the result of a registration operation.
    :param status: The status of the operation.
    :param details: The details of the operation.
    :param token: The token to track batch operations. None if not a batch operation.
    """
    status: Tuple[int, str]
    details: str = ""
    info: StatusResult | None = None


class SessionManager:
    """
    A class to manage a session with the EIDR API, using a config file.
    Maintains a list of tokens for the session, and exposes methods to interact with the API.
    """
    driver: API_Driver = None
    tokens: List[str] = []
    global parser
    global json_parser

    def __init__(self, driver: API_Driver):
        self.driver = driver

    @classmethod
    def from_default(cls):
        """
        Create a SessionManager instance using the default config file.
        :return:
            SessionManager: An instance of SessionManager with the default API_Driver.
        """
        return cls(API_Driver.from_default(config_file=CONFIG_PATH))

    @classmethod
    def from_dict(cls, config: ConfigDict):
        """
        Create a SessionManger instance using a dict
        :return:
            SessionManger: An instance of SessionManger with the default API_Driver.
        """
        return cls(API_Driver.from_dict(config))

    def post(self, req: RegistryRequest | NoOperationRequest, res_type: ResponseType = ResponseType.DEFAULT,
             params: dict = None):
        """
        Post a request to the EIDR API.
        :param req: The request to post.
        :param res_type: Unused.
        :param params: Extra HTTP parameters to pass over
        :return:
            ResponseReader: The response from the API wrapped in a helper class.
        """
        raw = self.driver.post_raw(req.xml, req.name, params=params).content.decode("utf-8")
        res = ResponseReader(raw)
        if res.token:
            self.tokens.append(res.token)
        return res

    def resolve(self, id: str, resolve_mode: str | ResolveRecordMode = ResolveRecordMode.FULL, out_path: Path = None,
                return_dataclass: bool = False) -> dict | FullMetadata | SelfDefinedMetadata | InheritedMetadata | SimpleMetadata | ProvenanceMetadata | KernelMetadata | AlternateIds | LinkedAlternateIds:
        """
        Resolve an ID to a FullMeta object (will be streamlined into file paradigm).
        Resolution mode -> Return type (in the case return_dataclass is True)
        ----
        Full -> FullMetadata, SelfDefined -> SelfDefinedMetadata, Inherited -> InheritedMetadata,
        Simple -> SimpleMetadata, Provenance -> ProvenanceMetadata, DOIKernel -> KernelMetadata,
        AlternateId -> AlternateIds, LinkedAlternateId -> LinkedAlternateIds


        :param id: The ID to resolve.
        :param resolve_mode: The type of response desired.
        :param out_path: The path to save the resolved object to. (optional)
        :param return_dataclass: Whether to return the dataclass or a dictionary representation.
        :return:
            Dict | Dataclass: A dictionary representation of the record, optionally may return a xsdata autogenerated class
        """
        if isinstance(resolve_mode, Enum):
            resolve_mode = resolve_mode.value
        res = self.driver.get_object(id, resolve_mode).decode("utf-8")
        raw = parser.from_string(res)

        info = instance_to_dict(raw)
        if out_path:
            ...
        return raw if return_dataclass else info

    def query(self, q: RegistryRequest[Query], as_file: bool = False) -> Tuple[List[SimpleWrapper] | List[str], str]:
        """
        Query the EIDR API with a query request.
        :param q: A RegistryRequest object containing the query. Must be of type Query.
        :param as_file: Whether to save the results to a file named "query_results.json".
        :return:
            Tuple[List[SimpleMetadata] | List[str], str]:
                A tuple containing a list of SimpleMetadata and a continuation token, OR
                A tuple containing a list of EIDR ids and a continuation token.

        """
        if q.name != "query":
            raise ValueError("Must call query with query request")
        res_type = q.response_type
        if isinstance(res_type, Enum):
            res_type = res_type.value

        res = self.post(q, params={"type": res_type})
        if res.status[0] != 0:
            # print(res.obj)
            raise RuntimeError("Got bad status {}".format(res.status))
        check_err(res)
        q_res = res.get_field("query_results")
        matched = None
        if res_type == Query.QueryResponseType.ID.value:
            matched = [doi.value for doi in q_res.id]
        else:
            matched = [SimpleWrapper(data, driver=self.driver) for data in q_res.simple_metadata]
        if as_file:
            with open("query_results.json", "w") as f:
                out = instance_to_dict(res.obj, include_type=False)
                filtered = {key: val for key, val in out.items() if val not in [None, []]}
                json.dump(filtered, f, indent=4)
        return matched, q_res.continuation_token

    def status(self, s: RegistryRequest[StatusRequest],
               response_map: Dict[int, Callable[[int, str], Any]] = default_responses,
               default_handler: Callable[[int, str], Any] | None = crash_on_status
               ) -> Tuple[List[dict], str]:
        """
        Get the status of an operation using the provided service.
        :param s: The status request to post.
        :param response_map: A dictionary mapping status codes to response handlers (int, str) -> Any. Returned value stored in key "extra"
        :param default_handler: A default handler for status codes not in the status_handlers. Defaults to crashing on unhandled status.
        :return:
            Tuple[List[dict], str]: A tuple containing a list of operation statuses and a continuation token.
        """
        if s.name != "status":
            raise ValueError("Must call status with status request")
        # print(s.xml)
        res = self.post(s)
        # print(res.obj)
        if res.status[0] != 0:
            raise RuntimeError("Got bad status {}".format(res.status))
        check_err(res)

        operation_stats = handle_status_results(res, status_handlers=response_map, default_handler=default_handler)

        # Append tokens that are not already in the list (making sure they're not empty strings)
        self.tokens += [stat["token"] for stat in operation_stats if stat["token"] not in self.tokens and stat["token"]]
        status_res = res.get_field("request_status_results")

        return operation_stats, status_res.continuation_token

    def future_status(self, s: RegistryRequest[StatusRequest], wait: float = 1, retries: int = 10) -> List[Future]:
        """
        Get the status of an operation, for use in an async pipeline.
        :param s: The status request to post.
        :param wait: The time to wait between retries in seconds.
        :param retries: The number of retries to attempt.
        :return:
            List[Future]: A list of futures representing the status of the operation.
        """
        if s.name != "status":
            raise ValueError("Must call status with status request")
        res = self.post(s)
        if res.status[0] != 0:
            raise RuntimeError("Got bad status {}".format(res.status))
        check_err(res)
        status_res = res.get_field("request_status_results")
        operation_stats = [{
            "token": op_res.token,
            "status": (op_res.status.code.value, op_res.status.type_value.value),
            "details": (op_res.status.details_code, op_res.status.details)
        } for op_res in status_res.operation_status] if status_res else []
        futures = []
        for op in operation_stats:
            future = asyncio.create_task(self.poll_status(op["token"], wait, retries))
            futures.append(future)
        return futures

    def service_resolve(self, id: str, service_doi: str | ResolveUserMode = ResolveUserMode.FULL,
                        followAlias: bool = True):
        """
        Resolve a service to a ServiceMeta object.
        :param id: ID of the service in the EIDR registry.
        :param service_doi: The type of response desired
        :param followAlias: Whether to follow the alias of the service when resolving.
        :return:
            ServiceMeta: The resolved ServiceMeta object.
        """
        res = self.driver.get_video_service(id, service_doi, followAlias)
        return ServiceMeta.from_string(res)

    def service_query(self, s: NoOperationRequest):
        """
        Query the EIDR API with a service query request.
        :param s: The service query/queries request to post.
        :return:
            List[ServiceMeta]: A list of ServiceMeta objects representing the services that match the query.
        """
        if s.name != "service/query":
            raise ValueError("Must call service query with service query request")
        res = self.post(s, res_type=ResponseType.SERVICE)
        check_err(res)
        # print(res)
        q_res = res.obj
        if q_res.continuation_token is not None:
            self.tokens.append(q_res.continuation_token)
        out = [ServiceMeta(s) for s in q_res.service]

        return out

    async def poll_status(self, token: str, wait: float, retries: int):
        """
        Poll the status of an operation using the provided token.
        :param token: The token assigned to the operation to poll.
        :param wait: The time to wait between retries in seconds.
        :param retries: The number of retries to attempt.
        :return:
            dict: The status of the operation(s).
        """
        for i in range(retries):
            s = StatusRequest(token=token)
            req = RegistryRequest(operations=[s])
            res, cont = self.status(req)
            status, _ = res[0]["status"]
            if status == 2:
                return res[0]
            await asyncio.sleep(wait)
        print("Failed to get status")
        return None

    def party_resolve(self, party_id: str,
                      resolve_mode: str | ResolveUserMode | ResolvePartyMode = ResolvePartyMode.FULL):
        """
        Resolve a party to a PartyMeta object.
        :param party_id: The ID of the party to resolve.
        :param resolve_mode: The type of response desired. (doi | full)
        :return:
            PartyMeta: The resolved PartyMeta object.
        """
        res = self.driver.get_party(party_id, resolve_mode)
        return PartyMeta.from_string(res)

    def user_resolve(self, user_doi: str, resolve_mode: str | ResolveUserMode = ResolveUserMode.FULL):
        """
        Resolve a user.
        :param user_doi: The ID of the user to resolve.
        :param resolve_mode: The type of response desired.
        :return:
            ResponseReader: The response from the API wrapped in a helper class.
        """
        res = self.driver.get_party(_user_doi=user_doi, resolve_mode=resolve_mode)
        response = ResponseReader(res)
        check_err(response)
        return response

    def change_user_password(self, user_doi: str, password: str):
        """
        Change the password of a user. The user's current credentials must be provided in the config file.
        :param user_doi: The ID of the user to change the password for.
        :param password: The new password to set for the user.
        :return:
        """
        endpoint = "user/password/{}".format(user_doi)
        response = self.driver.post_raw("", endpoint, {"password": password})
        response = ResponseReader(response.content.decode("utf-8"))
        return response

    # TODO: check
    def party_query(self, p: NoOperationRequest[PartyQuery]) -> List[PartyMeta | str]:
        """
        Query the EIDR API with a party query request.
        :param p: The party query request to post.
        :param full: Whether to return the full party metadata or just the ID.
        :return:
            List[PartyMeta | str]: A list of PartyMeta objects (or IDs) representing the parties that match the query.
        """
        if p.name != "party/query":
            raise ValueError("Must call party query with party query request")

        res: ResponseReader = self.post(p, res_type=ResponseType.PARTY,
                                        params={"type": p.response_type}) if p.response_type \
            else self.post(p, res_type=ResponseType.PARTY)
        check_err(res)

        matches = [PartyMeta(match) for match in
                   res.get_field("party_id")] if p.response_type == PartyQuery.PartyResponseType.ID.value else \
            [PartyMeta(match) for match in res.get_field("party")]

        if res.continuation_token:
            self.tokens.append(res.continuation_token)
        return matches

    def permissions(self, object_id: str, acl_type: str | ACL_Type = ACL_Type.MODIFY):
        """
        Get a list of which parties have permissions to perform the according operation.
        :param object_id: The ID of the object to get permissions for.
        :param acl_type: The type of permissions to get.
        :return:
            List[str]: A list of party IDs that have permissions to perform the operation.
        """
        res = ResponseReader(self.driver.get_permissions(object_id, acl_type))
        check_err(res)
        if res.status[0] != 0:
            raise RuntimeError("Got bad status {}".format(res.status))
        out: List[str] = res.get_field("party_id")
        return out

    def modification_base(self, object_id: str, modification_type: str | ModifyType):
        """
        Get the base metadata to perform a modification from.
        :param object_id: The ID of the object to get the base metadata for.
        :param modification_type: The type of modification to perform.
        :return:
            dict: A dictionary containing the base metadata for modification.
        """
        if isinstance(modification_type, Enum):
            modification_type = modification_type.value
        base = modification_type.lower().replace("create", "")
        res = ResponseReader(self.driver.get_modification_base(object_id, modification_type))
        check_err(res)
        if res.status[0] != 0:
            raise RuntimeError("Got bad status {}".format(res.status))
        out: dict = instance_to_dict(res.get_field(base))
        del out["_dataclass"]
        return out

    def register_immediate(self, req_obj: RegistryRequestSingle[RegistrationService]) -> StatusResult:
        if req_obj.name != "register":
            raise ValueError("Must call register with register request")
        self.driver.config.set_header('Immediate-Response', 'true')
        resp = self.post(req_obj)

        if resp.status[0] == 0:
            result = handle_status_results(resp, default_handler=None, status_handlers=None)[0]
            if len(result):
                return result
            else:
                raise ValueError("No results in register response, something is wrong with the SDK or the registry.")
        raise BadStatusError(status=resp.status, details="")

    def register(self, req_obj: RegistryRequestSingle[RegistrationService]) -> BatchStatusResult:
        """
        Perform a registration operation in the EIDR Registry.
        :param req_obj: The request object to be passed to the registration service.
        :param immediate_resp: Enable the Immediate Response header in the request
        :return:
            Tuple[Tuple[int, str], str]: A tuple containing the status (code, details) and the token to track batch operations.
        """
        if req_obj.name != "register":
            raise ValueError("Must call register with register request")

        self.driver.config.remove_header('Immediate-Response')
        resp = self.post(req_obj)
        result = handle_batch_results(resp, default_handler=None, status_handlers={
            1: lambda code, details: "I just batched all over myself",
        })[0]
        return result

    def register_batch(self, req_obj: RegistryRequest[RegistrationService]) -> BatchStatusResult:
        self.driver.config.remove_header('Immediate-Response')
        resp = self.post(req_obj)
        results = handle_batch_results(resp, default_handler=None, status_handlers={
            1: lambda code, details: "I just batched all over myself",
        })

        return results[0]


class BadStatusError(Exception):
    status: Tuple[int, str]
    details: str

    def __init__(self, msg: str = "Bad status", status: Tuple[int, str] = (-1, "Unknown"),
                 details: str = "Developer did not provide details"):
        super().__init__(msg + f"\n\tGot status: {status}")
        self.status = status
        self.details = details


# token: str, status: Tuple(int, str)

# token, status_result = register_batch(records)
# ses.status(... token ...)

def test_permissions():
    ses = SessionManager.from_default()
    res = ses.permissions("10.5240/8B55-F9AA-007F-B18E-C000-6", acl_type=ACL_Type.MODIFY)
    print(res)


def test_query():
    ses = SessionManager.from_default()
    exp = Query.base_obj_expression(
        resource_name="Hilter Von StrongBerg's Golden Freddy"
    )
    q = Query(
        response_type=Query.QueryResponseType.ID,
        expression=exp,
        page_num=1,
        page_size=100
    )
    res = ses.query(RegistryRequest(
        operations=[q]
    ))
    print(res)


def test_modification_base():
    ses = SessionManager.from_default()
    res = ses.modification_base("10.5240/8B55-F9AA-007F-B18E-C000-6", ModifyType.CREATE_EDIT)
    out = json.dumps(res, indent=4)
    with open("mod_base_test.json", "w") as f:
        f.write(out)
    print(out)


def test_status_req():
    ses = SessionManager.from_default()

    stat = ses.register_immediate(RegistryRequestSingle(Delete("10.5240/8B55-F9AA-007F-B18E-C000-6")))

    # if stat:
    #     s = StatusRequest(token=stat["token"])
    #     res = ses.status(RegistryRequest(operations=[s]), default_handler=lambda code, details: "Testing",
    #                      response_map={
    #                          0: lambda code, details: "Success",
    #                          3: lambda code, details: "Booyeah Booyeah Booyeah"
    #                      })
    #     print(res)
    print(stat)


def test_resolve():
    ses = SessionManager.from_default()
    # res = ses.resolve("10.5240/8B55-F9AA-007F-B18E-C000-6", ResolveRecordMode.SIMPLE, return_dataclass=True)
    for option in ResolveRecordMode:
        res = ses.resolve("10.5240/8B55-F9AA-007F-B18E-C000-6", option)
        print(res)


if __name__ == "__main__":
    ...
    # test_permissions()
    # test_query()
    # test_modification_base()
    test_status_req()
