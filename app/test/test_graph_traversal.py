import unittest

import app.services.graph_traversal as graph
from app.driver import API_Driver, to_pretty_xml
from app.manager import SessionManager, ResolveRecordMode
from app.scheme.org.eidr.schema.asset_doitype import AssetDoitype
from app.scheme.org.eidr.schema.status_type_type import StatusTypeType


class GraphTraversal(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.session = SessionManager.from_default()
        cls.driver = cls.session.driver
        cls.traversal = graph.GraphTraversal(driver=cls.driver)

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
        res = self.driver.post_raw(
            xml, "object/graph"
        )
        result_string = to_pretty_xml(res.content)
        self.assertEqual(True, result_string is not None)

    def test_find_descendents(self):
        doi = "10.5240/8B55-F9AA-007F-B18E-C000-6"
        response_reader, err = self.traversal.find_descendants(doi)
        if err is not None:
            self.fail(err)

        _, status_value = response_reader.status
        self.assertEqual(StatusTypeType.SUCCESS.value, status_value, "Unsuccessful Request")

    def test_find_ancestors(self):
        doi = "10.5240/8B55-F9AA-007F-B18E-C000-6"
        doi = AssetDoitype(doi)
        response_reader, err = self.traversal.find_ancestors(doi)
        if err is not None:
            self.fail(err)
        _, status_value = response_reader.status
        self.assertEqual(StatusTypeType.SUCCESS.value, status_value, "Unsuccessful Request")

    def test_remotest_ancestor(self):
        doi = "10.5240/8B55-F9AA-007F-B18E-C000-6"
        doi = AssetDoitype(doi)
        response_reader, err = self.traversal.get_remotest_ancestor(doi)
        if err is not None:
            self.fail(err)
        _, status_value = response_reader.status
        self.assertEqual(StatusTypeType.SUCCESS.value, status_value, "Unsuccessful Request")

    def test_get_leaf_descendants(self):
        doi = "10.5240/8B55-F9AA-007F-B18E-C000-6"
        doi = AssetDoitype(doi)
        response_reader, err = self.traversal.get_leaf_descendants(doi)
        if err is not None:
            self.fail(err)
        _, status_value = response_reader.status
        self.assertEqual(StatusTypeType.SUCCESS.value, status_value, "Unsuccessful Request")

    def test_get_lightweight_relationship(self):
        doi = "10.5240/8B55-F9AA-007F-B18E-C000-6"
        doi = AssetDoitype(doi)
        response_reader, err = self.traversal.get_lightweight_relationships(doi)
        if err is not None:
            self.fail(err)

        _, status_value = response_reader.status
        self.assertEqual(StatusTypeType.SUCCESS.value, status_value, "Unsuccessful Request")

    def test_get_dependants(self):
        doi_THEGODFATHER = "10.5240/4911-14D5-3C9F-7BE1-AF9D-X"
        response_reader, err = self.traversal.get_dependants(doi_THEGODFATHER)
        if err is not None:
            self.fail(err)
        _, status_value = response_reader.status
        self.assertEqual(StatusTypeType.SUCCESS.value, status_value, "Unsuccessful Request")

    def test_get_children(self):
        doi = "10.5240/5448-E7EB-CB49-E03F-999A-L"
        response_reader, err = self.traversal.get_children(doi)
        if err is not None:
            self.fail(err)
        _, status_value = response_reader.status
        self.assertEqual(StatusTypeType.SUCCESS.value, status_value, "Unsuccessful Request")

    def test_get_parent(self):
        doi = "10.5240/5448-E7EB-CB49-E03F-999A-L"
        doi_THEGODFATHER = "10.5240/4911-14D5-3C9F-7BE1-AF9D-X"
        response_reader, err = self.traversal.get_parent(doi_THEGODFATHER)
        if err is not None:
            self.fail(err)
        _, status_value = response_reader.status
        self.assertEqual(StatusTypeType.SUCCESS.value, status_value, "Unsuccessful Request")

    def test_get_series_ancestry(self):
        doi = "10.5240/5448-E7EB-CB49-E03F-999A-L"
        response_reader, err = self.traversal.get_series_ancestry(doi)
        if err is not None:
            self.fail(err)
        _, status_value = response_reader.status
        self.assertEqual(StatusTypeType.SUCCESS.value, status_value, "Unsuccessful Request")

    def test_find_descendants_with_extended_family(self):
        doi = "10.5240/8B55-F9AA-007F-B18E-C000-6"
        response_reader, err = self.traversal.find_descendants(doi, extended_family=True)
        if err is not None:
            self.fail(err)
        _, status_value = response_reader.status
        self.assertEqual(StatusTypeType.SUCCESS.value, status_value, "Unsuccessful Request with extended_family")

    def test_find_ancestors_with_filters(self):
        from app.scheme.org.eidr.schema import ReferentType
        doi = "10.5240/8B55-F9AA-007F-B18E-C000-6"
        response_reader, err = self.traversal.find_ancestors(
            doi,
            referent_type_filter=[ReferentType.MOVIE]
        )
        if err is not None:
            self.fail(err)
        _, status_value = response_reader.status
        self.assertEqual(StatusTypeType.SUCCESS.value, status_value, "unsuccessful Request with referent type filter")

    def test_find_descendants_with_invalid_doi(self):
        with self.assertRaises(ValueError):
            self.traversal.find_descendants("")

    # TODO:Find video service ids to use

    # def test_video_service_get_parent(self):
    #     doi = "10.5239/170B-1D36"
    #     response_reader, err = self.traversal.video_service_get_parent(doi)
    #     if err is not None:
    #         self.fail(err)
    #     _, status_value = response_reader.status
    #     self.assertEqual(StatusTypeType.SUCCESS.value, status_value, "Unsuccessful Request")
    #
    #
    # def test_video_service_get_children(self):
    #     doi = "10.5239/170B-1D36"
    #     response_reader, err = self.traversal.video_service_get_children(doi,all_children=True)
    #     if err is not None:
    #         self.fail(err)
    #     _, status_value = response_reader.status
    #     self.assertEqual(StatusTypeType.SUCCESS.value, status_value, "Unsuccessful Request")
    #


if __name__ == '__main__':
    unittest.main()
