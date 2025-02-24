import unittest

import app.services.graph_traversal as graph
from app.services.res import Response
from app.driver import API_Driver, to_pretty_xml
from    app.scheme.org.eidr.schema.graph.find_descendants_type import FindDescendantsType
from    app.scheme.org.eidr.schema.graph.find_ancestors_type import FindAncestorsType
from    app.scheme.org.eidr.schema.asset_doitype import AssetDoitype
from    app.scheme.org.eidr.schema.response import ResponseType
from    app.scheme.org.eidr.schema.status_type_type import StatusTypeType


class GraphTraversal(unittest.TestCase):


    def test_example_return(self):
        driver = API_Driver.from_default()
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
        res = driver.post_raw(
            xml, "object/graph"
        )
        result_string = to_pretty_xml(res.content)
        print(result_string)
        self.assertEqual(True, result_string is not None)

    def test_find_descendents(self):
        driver = API_Driver.from_default()
        traversal = graph.GraphTraversal()
        doi = "10.5240/8B55-F9AA-007F-B18E-C000-6"
        req = traversal.find_descendants(doi)
        res = driver.post_raw(
            req,
            "object/graph"
        )
        xml = to_pretty_xml(res.content)
        response: ResponseType = Response.from_xml(xml)
        self.assertEqual(StatusTypeType.SUCCESS.value, response.status.type_value.value, "Unsuccessful Request")
        print(response)

    def test_find_descendants_with_Dict(self):
        driver = API_Driver.from_default()
        traversal = graph.GraphTraversal()
        doi_endgame = "10.5240/C745-6B21-0FC0-70A0-9ECE-6"
        doi_infinity_war = "10.5240/ACF2-FF3C-9F47-02A0-EA40-H"
        doi = AssetDoitype(doi_infinity_war)
        find_descendants = FindDescendantsType(
            id=doi,
            referent_type=None,
            relationship_type=None,
            structural_type=None,
        )
        req = traversal.find_descendants(find_descendants=find_descendants)
        res = driver.post_raw(
            req,
            "object/graph"
        )
        xml = to_pretty_xml(res.content)
        response: ResponseType = Response.from_xml(xml)
        self.assertEqual(StatusTypeType.SUCCESS.value, response.status.type_value.value, "Unsuccessful Request")
        print(response)

    def test_find_ancestors(self):
        driver = API_Driver.from_default()
        traversal = graph.GraphTraversal()

        doi = "10.5240/8B55-F9AA-007F-B18E-C000-6"
        doi = AssetDoitype(doi)
        req = traversal.find_ancestors(doi)
        res = driver.post_raw(
            req,
            "object/graph"
        )
        xml = to_pretty_xml(res.content)
        response: ResponseType = Response.from_xml(xml)
        self.assertEqual(StatusTypeType.SUCCESS.value, response.status.type_value.value, "Unsuccessful Request")
        print(response)

    def test_find_ancestors_with_Dict(self):
        driver = API_Driver.from_default()


        traversal = graph.GraphTraversal()
        doi_endgame = "10.5240/C745-6B21-0FC0-70A0-9ECE-6"
        doi_infinity_war = "10.5240/ACF2-FF3C-9F47-02A0-EA40-H"
        doi = AssetDoitype(doi_endgame)
        find_ancestors = FindAncestorsType(
            id=doi,
            referent_type=None,
            relationship_type=None,
            structural_type=None,
        )
        req = traversal.find_ancestors(find_ancestors=find_ancestors)
        print(req)
        res = driver.post_raw(
            req,
            "object/graph"

        )
        xml = to_pretty_xml(res.content)
        response: ResponseType = Response.from_xml(xml)
        self.assertEqual(StatusTypeType.SUCCESS.value, response.status.type_value.value, "Unsuccessful Request")
        print(response)

    def test_get_dependants(self):
        driver = API_Driver.from_default()
        traversal = graph.GraphTraversal()
        bleach_186= "10.5240/CED5-C017-98C4-95D0-89B7-G"
        bleach_series= "	10.5240/4911-14D5-3C9F-7BE1-AF9D-X"
        doi = AssetDoitype(bleach_series)
        req = traversal.get_dependants(doi)
        print(req)
        res = driver.post_raw(
            req,
            "object/graph"
        )
        xml = to_pretty_xml(res.content)
        print(xml)
        response: ResponseType = Response.from_xml(xml)
        self.assertEqual(StatusTypeType.SUCCESS.value, response.status.type_value.value, "Unsuccessful Request")
        print(response)


if __name__ == '__main__':
    unittest.main()
