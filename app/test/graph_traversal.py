import unittest

import app.services.graph_traversal as graph
from app.scheme.org.eidr.schema import simple_info_type
from app.driver import API_Driver, to_pretty_xml
from app.scheme.org.eidr.schema.graph.find_descendants_type import FindDescendantsType
from app.scheme.org.eidr.schema.graph.find_ancestors_type import FindAncestorsType
from app.scheme.org.eidr.schema.asset_doitype import AssetDoitype
from app.scheme.org.eidr.schema.response import ResponseType
from app.scheme.org.eidr.schema.status_type_type import StatusTypeType
from app.scheme.org.eidr.schema.simple_info_type import SimpleInfoType
from app.scheme.org.eidr.schema.registrations_type import RegistrationsType
from app.scheme.org.eidr.schema.create_basic_data_type import CreateBasicDataType, CreationFullInfo
from app.services.res import ResponseReader
from app.services.simple_metadata import SimpleMetadata

from typing import Tuple, Any


class GraphTraversal(unittest.TestCase):

    driver = API_Driver.from_default()
    traversal = graph.GraphTraversal(driver)

    def test_example_return(self):
        ## Found sol no empty chars befrore this line -> <?xml version="1.0" encoding="UTF-8"?>
        xml = """<?xml version='1.0' encoding='UTF-8'?>
<Request xmlns="http://www.eidr.org/schema"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<Operation>
<GetRemotestAncestor>
<ID>10.5240/8B55-F9AA-007F-B18E-C000-6</ID>
</GetRemotestAncestor>
</Operation>
</Request>
            """
        print(xml)
        res = self.driver.post_raw(
            xml, "object/graph"
        )
        result_string = to_pretty_xml(res.content)
        print(result_string)
        self.assertEqual(True, result_string is not None)

    def test_find_descendents(self):
        doi = "10.5240/8B55-F9AA-007F-B18E-C000-6"
        req = self.traversal.find_descendants(doi)
        res = self.driver.post_raw(
            req,
            "object/graph"
        )
        xml = to_pretty_xml(res.content)
        response: SimpleInfoType = response.obj
        self.assertEqual(StatusTypeType.SUCCESS.value, response.status.type_value.value, "Unsuccessful Request")
        print(response)

    def test_find_descendants_with_Dict(self):
        doi_endgame = "10.5240/C745-6B21-0FC0-70A0-9ECE-6"
        doi_infinity_war = "10.5240/ACF2-FF3C-9F47-02A0-EA40-H"
        doi = AssetDoitype(doi_infinity_war)
        find_descendants = FindDescendantsType(
            id=doi,
            referent_type=None,
            relationship_type=None,
            structural_type=None,
        )
        req = self.traversal.find_descendants(find_descendants=find_descendants)
        res = self.driver.post_raw(
            req,
            "object/graph"
        )
        xml = to_pretty_xml(res.content)
        response: Response = Response.from_xml(xml)
        response: SimpleInfoType = response.obj
        self.assertEqual(StatusTypeType.SUCCESS.value, response.status.type_value.value, "Unsuccessful Request")
        print(response)

    def test_find_ancestors(self):
        doi = "10.5240/8B55-F9AA-007F-B18E-C000-6"
        doi = AssetDoitype(doi)
        response:Tuple[ResponseReader,Any] = self.traversal.find_ancestors(doi)
        if response[1] is not None:
            print("Error finding ancestor",response[1])
        response_reader:ResponseReader = response[0]
        self.assertEqual(StatusTypeType.SUCCESS.value, response_reader.status[1], "Unsuccessful Request")
        print(response_reader.get_simple_metaData())

    def test_find_ancestors_with_Dict(self):
        doi_endgame = "10.5240/C745-6B21-0FC0-70A0-9ECE-6"
        doi_infinity_war = "10.5240/ACF2-FF3C-9F47-02A0-EA40-H"
        doi = AssetDoitype(doi_endgame)
        find_ancestors = FindAncestorsType(
            id=doi,
            referent_type=None,
            relationship_type=None,
            structural_type=None,
        )
        req = self.traversal.find_ancestors(find_ancestors=find_ancestors)
        print(req)
        res = self.driver.post_raw(
            req,
            "object/graph"

        )
        xml = to_pretty_xml(res.content)
        response: Response = Response.from_xml(xml)
        response: SimpleInfoType = response.obj
        self.assertEqual(StatusTypeType.SUCCESS.value, response.status.type_value.value, "Unsuccessful Request")
        print(response)

    def test_get_dependants(self):

        """ DOI the id of a EIDR record  """
        doi_THEGODFATHER = "10.5240/4911-14D5-3C9F-7BE1-AF9D-X"

        """ Request Object For Communicating with Eidr API   """
        req = self.traversal.get_dependants(doi_THEGODFATHER)
        res =  self.driver.post_raw(req, "object/graph")

        xml = to_pretty_xml(res.content)
        print(xml,"hgkhgkgkhk")

        """ Reponse Containing SimpleMetaData  """
        response: Response = Response.from_xml(xml)
        response: SimpleInfoType = response.obj

        """ Validating The Success Of the Request  """

        self.assertEqual(StatusTypeType.SUCCESS.value, response.status.type_value.value, "Unsuccessful Request")


if __name__ == '__main__':
    unittest.main()
