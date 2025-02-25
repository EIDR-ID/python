from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from app.scheme.org.eidr.schema import response, response_type
from app.driver import test_query

from util import attempt

config = ParserConfig()
context = XmlContext()
parser = XmlParser(context=context, config=config)
ns = {"": "http://www.eidr.org/schema"}


class ResponseReader:
    obj = None

    def __init__(self, res_str):
        self.obj = parser.from_string(res_str, response.Response, ns)

    @classmethod
    def from_xml(cls, xml: str):
        return ResponseReader(xml)

    def __get_item__(self, key: str):
        return self.get_field(key)

    def get_field(self, key: str):
        print(self.obj)
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



def test():
    r = test_query()
    res = ResponseReader.from_xml(test_query())
    res, err = res.get_fields(
        "query_results",
        "status",
        "version"
    ), None
    print(res)


test()
