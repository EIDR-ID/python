from enum import Enum
from typing import Tuple

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig

import app.driver as d
from app.scheme.org.doi.pkg_2010.doischema import KernelMetadata
from app.scheme.org.eidr.schema import ServiceQueryResults, PartyQueryResults, PartyDoilistType, AdminResponse

from app.scheme.org.eidr.schema.response import Response
from app.services import Query, RegistryRequest
from app.services.simple_metadata import SimpleMetadata
from app.scheme.org.eidr.schema.simple_info import SimpleInfo

#from app.util import attempt

def attempt(func):
    try:
        return func(), None
    except Exception as e:
        return None, e

config = ParserConfig()
context = XmlContext()
parser = XmlParser(context=context, config=config)
ns = {"": "http://www.eidr.org/schema"}


class ResponseType(Enum):
    DEFAULT = Response
    SERVICE = ServiceQueryResults
    KERNELMETADATA = KernelMetadata
    PARTY = PartyQueryResults
    PERMISSIONS = PartyDoilistType

class ResponseReader:
    obj: Response | ServiceQueryResults | KernelMetadata | AdminResponse | PartyDoilistType = None
    token: str | None = None
    status: Tuple[int, str] = None
    continuation_token: str | None = None
    admin_response: bool = False
    def __init__(self, res_str, driver: d.API_Driver = None):
        self.__dir__()

        self.obj = parser.from_string(res_str, None, ns)
        self.driver = driver
        if hasattr(self.obj, "request_status") and self.obj.request_status:
            self.token = self.obj.request_status.token

        if isinstance(self.obj, AdminResponse):
            self.admin_response = True
            self.status = self.obj.code.value, self.obj.type_value.value
        elif hasattr(self.obj, "status") and self.obj.status:
            self.status = self.obj.status.code.value, self.obj.status.type_value.value
        else:
            self.status = 0, "Status Unavailable"

    @classmethod
    def from_xml(cls, xml: str):
        return ResponseReader(xml)

    def __get_item__(self, key: str):
        return self.get_field(key)

    def get_field(self, key: str):
        res, err = attempt(lambda: getattr(self.obj, key))
        if err is not None:
            raise err
        return res

    def get_fields(self, *kwargs):
        out = []
        for key in kwargs:
            f = self.get_field(key)
            out.append(f)
        return out

    def get_simple_metaData(self, ) -> list[SimpleMetadata]:
        simple_metadata: list[SimpleInfo] = self.get_field("simple_metadata")
        simpleInfo: list[SimpleMetadata] = []
        for i in simple_metadata:
            simpleInfo.append(SimpleMetadata(i, self.driver))
        return simpleInfo


def test_query():
    driver = d.API_Driver.from_default()
    exp = Query.base_obj_expression(
        release_date="2005"
    )
    # print(exp)
    q = Query(
        expression=exp,
        page_num=1,
        page_size=1
    )

    res = driver.post(RegistryRequest(
        operations=[q]
    ))

    return d.to_pretty_xml(res.content)


def test():
    r = ResponseReader.from_xml(test_query())
    res, err = r.get_fields(
        "query_results",
        "status",
        "version"
    ), None
    print(res)
    print("SHITNING", r.status)


#test()
