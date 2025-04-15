import asyncio
from asyncio import Future
from enum import Enum
from typing import List, Tuple, TypedDict

from requests import Session
from xsdata.formats.dataclass.parsers.config import ParserConfig

from app.scheme.org.eidr.schema import RegistrantType, PartyDoilistType, PartyIdlist
from app.services import RegistryRequest, ServiceBase, ResponseReader, Query, StatusRequest, Delete
from app.driver import API_Driver, ResolveMode, ACL_Type
from app.services.metadata import BaseObjectMeta, FullMeta, ServiceMeta, PartyMeta
from app.services.party_query import PartyQuery
from app.services.res import test_query, parser, config
from app.services.service_query import NoOperationRequest, ServiceQuery
from app.services.simple_metadata import SimpleMetadata
from app.services.res import ResponseType
from app.scheme.org.eidr.schema.base_object_info_type import BaseObjectInfoType


class AdminResponseError(Exception):
    ...

def check_err(res: ResponseReader):
    if res.admin_response:
        raise AdminResponseError("\n\nAdmin Response Code {}: {}\n\t{}".format(*res.status, res.get_field("details")))


class SessionManager:
    driver: API_Driver = None
    tokens: List[str] = []

    def __init__(self, driver: API_Driver):
        self.driver = driver

    @classmethod
    def from_default(cls):
        return cls(API_Driver.from_default())

    def post(self, req: RegistryRequest | NoOperationRequest, res_type: ResponseType = ResponseType.DEFAULT,
             params: dict = None):
        raw = self.driver.post_raw(req.xml, req.name, params=params).content.decode("utf-8")
        res = ResponseReader(raw)
        if res.token:
            self.tokens.append(res.token)
        return res

    def resolve(self, id: str):
        res = self.driver.get_object(id)
        info = FullMeta.from_string(res.decode("utf-8"))
        # print(info.base_meta.resource_name)
        return info

    def query(self, q: RegistryRequest):
        if q.name != "query":
            raise ValueError("Must call query with query request")
        res = self.post(q)
        if res.status[0] != 0:
            #print(res.obj)
            raise RuntimeError("Got bad status {}".format(res.status))
        check_err(res)
        q_res = res.get_field("query_results")
        matched = [SimpleMetadata(data, driver=self.driver) for data in q_res.simple_metadata]
        return matched, q_res.continuation_token

    def status(self, s: RegistryRequest) -> Tuple[List[dict], str]:
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
        res = self.driver.get_video_service(id, service_doi, followAlias)
        return ServiceMeta.from_string(res)

    def service_query(self, s: NoOperationRequest):
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
        res = self.driver.get_party(party_id, resolve_mode)
        return PartyMeta.from_string(res)


    # TODO: check
    def party_query(self, p: NoOperationRequest, full: bool = True):
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
        res = ResponseReader(self.driver.get_permissions(object_id, acl_type))
        check_err(res)
        if res.status[0] != 0:
            raise RuntimeError("Got bad status {}".format(res.status))
        out: List[str] = res.get_field("party_id")
        return out

def test_permissions():
    ses = SessionManager.from_default()
    res = ses.permissions("10.5240/8B55-F9AA-007F-B18E-C000-6", acl_type=ACL_Type.MODIFY)
    print(res)

if __name__ == "__main__":
    test_permissions()