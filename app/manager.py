import asyncio
from asyncio import Future
from enum import Enum
from typing import List, Tuple, TypedDict

from requests import Session
from xsdata.formats.dataclass.parsers.config import ParserConfig

from app.scheme.org.eidr.schema import RegistrantType, PartyDoilistType, PartyIdlist, QueryResultsType
from app.services import RegistryRequest, ServiceBase, ResponseReader, Query, StatusRequest, Delete
from app.driver import API_Driver, ResolveMode, ACL_Type, ModifyType
from app.services.metadata import BaseObjectMeta, FullMeta, ServiceMeta, PartyMeta
from app.services.party_query import PartyQuery
from app.services.service_query import NoOperationRequest, ServiceQuery
from app.services.simple_metadata import SimpleMetadata
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


class SessionManager:
    """
    A class to manage a session with the EIDR API, using a config file.
    Maintains a list of tokens for the session, and exposes methods to interact with the API.
    """
    driver: API_Driver = None
    tokens: List[str] = []

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

    def resolve(self, id: str, resolve_mode: str | ResolveMode = ResolveMode.FULL) -> FullMeta:
        """
        Resolve an ID to a FullMeta object (will be streamlined into file paradigm).
        :param resolve_mode:
        :param id:
        :return:
            FullMeta: The resolved FullMeta object. (for now)
        """
        res = self.driver.get_object(id)
        info = FullMeta.from_string(res.decode("utf-8"))
        # print(info.base_meta.resource_name)
        return info

    def query(self, q: RegistryRequest, as_file: bool = False) -> Tuple[List[SimpleMetadata] | List[str], str]:
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
            #print(res.obj)
            raise RuntimeError("Got bad status {}".format(res.status))
        check_err(res)
        q_res = res.get_field("query_results")
        matched = None
        if res_type == Query.QueryResponseType.ID.value:
            matched = [doi.value for doi in q_res.id]
        else:
            matched = [SimpleMetadata(data, driver=self.driver) for data in q_res.simple_metadata]
        if as_file:
            with open("query_results.json", "w") as f:
                out = instance_to_dict(res.obj, include_type=False)
                filtered = {key: val for key, val in out.items() if val not in [None, []]}
                json.dump(filtered, f, indent=4)
        return matched, q_res.continuation_token

    def status(self, s: RegistryRequest) -> Tuple[List[dict], str]:
        """
        Get the status of an operation using the provided service.
        :param s: The status request to post.
        :return:
            Tuple[List[dict], str]: A tuple containing a list of operation statuses and a continuation token.
        """
        if s.name != "status":
            raise ValueError("Must call status with status request")
        #print(s.xml)
        res = self.post(s)
        #print(res.obj)
        if res.status[0] != 0:
            raise RuntimeError("Got bad status {}".format(res.status))
        check_err(res)
        status_res = res.get_field("request_status_results")
        #print(status_res)
        operation_stats = [{
            "token": op_res.token,
            "status": (op_res.status.code.value, op_res.status.type_value.value),
            "details": (op_res.status.details_code, op_res.status.details)
        } for op_res in status_res.operation_status] if status_res else []

        return operation_stats, status_res.continuation_token

    def future_status(self, s: RegistryRequest, wait: float = 1, retries: int = 10) -> List[Future]:
        """
        Get the status of an operation, for use in an async pipeline.
        :param s: The status request to post.
        :param wait: The time to wait between retries.
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

    def service_resolve(self, id: str, service_doi: str | ResolveMode = ResolveMode.FULL, followAlias: bool = True):
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
        #print(res)
        q_res = res.obj
        if q_res.continuation_token is not None:
            self.tokens.append(q_res.continuation_token)
        out = [ServiceMeta(s) for s in q_res.service]

        return out

    async def poll_status(self, token: str, wait: float, retries: int):
        """
        Poll the status of an operation using the provided token.
        :param token: The token assigned to the operation to poll.
        :param wait: The time to wait between retries.
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

    def party_resolve(self, party_id: str, resolve_mode: str | ResolveMode = ResolveMode.FULL):
        """
        Resolve a party to a PartyMeta object.
        :param party_id: The ID of the party to resolve.
        :param resolve_mode: The type of response desired.
        :return:
            PartyMeta: The resolved PartyMeta object.
        """
        res = self.driver.get_party(party_id, resolve_mode)
        return PartyMeta.from_string(res)

    def user_resolve(self, user_doi: str, resolve_mode: str | ResolveMode = ResolveMode.FULL):
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
    def party_query(self, p: NoOperationRequest, full: bool = True):
        """
        Query the EIDR API with a party query request.
        :param p: The party query request to post.
        :param full: Whether to return the full party metadata or just the ID.
        :return:
            List[PartyMeta | str]: A list of PartyMeta objects (or IDs) representing the parties that match the query.
        """
        if p.name != "party/query":
            raise ValueError("Must call party query with party query request")
        res: ResponseReader
        matches: List[PartyMeta | str] = []

        if full:
            res = self.post(p, res_type=ResponseType.PARTY, params={"type": "full"})
            check_err(res)
            matches = [PartyMeta(p) for p in res.get_field("party")]
        else:
            res = self.post(p, res_type=ResponseType.PARTY, params={"type": "ID"})
            check_err(res)
            matches = [PartyMeta(p) for p in res.get_field("party_id")]
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

    def register(self, new_record: RegistryRequest, immediate_resp: bool):
        """
        Register a new record with the EIDR API.
        :param new_record: The new record to register.
        :param immediate_resp:
        :return:
            Tuple[int, str]: A tuple containing the status code and details of the registration.
        """
        if new_record.name != "register":
            raise ValueError("Must call register with register request")
        if immediate_resp:
            self.driver.config.set_header('Immediate-Response', 'true')
        else:
            self.driver.config.remove_header('Immediate-Response')
        resp  = self.post(new_record)
        if resp.status[0] == 0:
            if operation_status := resp.obj.request_status_results.operation_status[0]:
                return operation_status
        return resp.status, resp.obj.status.details

def test_permissions():
    ses = SessionManager.from_default()
    res = ses.permissions("10.5240/8B55-F9AA-007F-B18E-C000-6", acl_type=ACL_Type.MODIFY)
    print(res)

def test_query():
    ses = SessionManager.from_default()
    exp = Query.base_obj_expression(
        release_date="2005"
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


if __name__ == "__main__":
    ...
    #test_permissions()
    #test_query()
    test_modification_base()