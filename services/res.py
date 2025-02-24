from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from scheme.org.eidr.schema import response, response_type
from app.driver import test_query

config = ParserConfig()
context = XmlContext()
parser = XmlParser(context=context, config=config)
ns = {"": "http://www.eidr.org/schema"}


class Response:
    def __init__(self):
        ...

    @classmethod
    def from_xml(cls, xml: str):
        return parser.from_string(xml, response.Response, ns)


# def test():
#     r = test_query()
#     print(r)
#     print(Response.from_xml(test_query()))
#
#
# test()
