from typing import List

from app.scheme.org.eidr.schema import RegistrantType
from app.services import RegistryRequest, ServiceBase, ResponseReader, Query, StatusRequest, Delete
from app.driver import API_Driver
from app.services.res import test_query
from app.services.simple_metadata import SimpleMetadata


class SessionManager:
    driver:API_Driver = None
    tokens:List[str] = []

    def __init__(self, driver: API_Driver):
        self.driver = driver

    def post(self, req: RegistryRequest):
        res = ResponseReader(self.driver.post_raw(req.xml, req.name).content.decode("utf-8"))
        if res.token:
            self.tokens.append(res.token)
        return res

    def query(self, q: RegistryRequest):
        if q.name != "query":
            raise ValueError("Must call query with query request")
        res = self.post(q)
        if res.status[0] != 0:
            print(res.obj)
            raise RuntimeError("Got bad status {}".format(res.status))
        q_res = res.get_field("query_results")
        matched = [SimpleMetadata(data,driver=self.driver) for data in q_res.simple_metadata]
        return matched, q_res.continuation_token

    def status(self, s: RegistryRequest):
        if s.name != "status":
            raise ValueError("Must call status with status request")
        print(s.xml)
        res = self.post(s)
        print(res.obj)
        status_res = res.get_field("request_status_results")
        print(status_res)
        operation_stats = [{
            "token": op_res.token,
            "status": (op_res.status.code.value, op_res.status.type_value.value),
            "details": (op_res.status.details_code, op_res.status.details)
        } for op_res in status_res.operation_status] if status_res else []

        return operation_stats, status_res.continuation_token

def test_ses_q():
    driver = API_Driver.from_default()
    ses = SessionManager(driver)
    exp = Query.base_obj_expression(
        release_date="2017"
    )
    ct = "AOIJAEIOJIEAWIOEJAO"
    q=RegistryRequest(
        operations=[Query(
            expression=exp,
            page_num=1,
            page_size=15,
            continuation_token=ct
        )]
    )
    res, continuation = ses.query(q)
    for r in res:
        print("\t", r.as_dict(), "\n")

    q2 = RegistryRequest(
        operations=[Query(
            page_num=2,
            page_size=15,
            continuation_token=continuation
        )]
    )
    res, continuation = ses.query(q2)
    print("!!!!")
    for r in res:
        print("\t", r.as_dict(), "\n")
    return res

def test_ses_d():
    driver = API_Driver.from_default()
    ses = SessionManager(driver)
    d=RegistryRequest(
        operations=[Delete(
            id="10.5240/BA24-7B2E-6DBB-D3BC-1721-2"
        )]
    )
    res = ses.post(d)
    print(res.obj, "\nADADDDA\n", ses.tokens[-1])
    return res

def test_status():
    token = "1741054324732003662"
    driver = API_Driver.from_default()
    ses = SessionManager(driver)
    s=RegistryRequest(
        operations=[StatusRequest(
            user_id="10.5238/cramos",
            page_number=1,
            page_size=10
        )]
    )
    res, _ = ses.status(s)
    for r in res:
        print("\t", r, "\n")


test_ses_q()
#test_status()