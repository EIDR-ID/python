from typing import Optional, Union
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from app.scheme.org.eidr.schema.request import Request
from app.scheme.org.eidr.schema.asset_doitype import AssetDoitype
import app.driver as Driver
from app.services.graph_traversal import GraphTraversal
import app.services.response_reader as ResponseReader
from typing import Tuple


class VideoServiceGraphTraversal:
    """
    A class to handle graph traversal operations for a given DOI.
    """

    def __init__(self, driver: Driver.API_Driver):
        self.driver = driver
        self.doi = None
        self.name = None
        self.serializer = XmlSerializer(config=SerializerConfig(indent="    "))
        self.ns_map = {"": "http://www.eidr.org/schema"}

    def get_children(
            self,
            doi: Optional[Union[str, AssetDoitype]] = None,
            all_children: bool = False
    ) -> Tuple[Optional['ResponseReader.ResponseReader'], Optional[ValueError]]:
        """
        """
        if doi is None:
            doi = self.validate_doi(self.doi)
        else:
            doi = self.validate_doi(doi)
        return self.validate_response(service_endpoint="service/children", doi=doi, all_children=all_children)

    def get_parent(
            self,
            doi: Optional[Union[str, AssetDoitype]] = None
    ) -> Tuple[Optional['ResponseReader.ResponseReader'], Optional[ValueError]]:
        """
        """
        if doi is None:
            doi = self.validate_doi(self.doi)
        else:
            doi = self.validate_doi(doi)
        return self.validate_response(service_endpoint="service/children", doi=doi, all_children=False)

    def validate_response(
            self,
            service_endpoint: str,
            doi: AssetDoitype,
            all_children: bool = False
    ) -> Tuple[Optional['ResponseReader.ResponseReader'], Optional[ValueError]]:
        """
        """
        response = self.driver.get_video_service_traversal(
            service_doi=doi,
            service_endpoint=service_endpoint,
            all_children=all_children
        )
        response.raise_for_status()
        xml = Driver.to_pretty_xml(response.content)
        response_reader: ResponseReader = ResponseReader.ResponseReader(res_str=xml, driver=self.driver)
        status_code, _ = response_reader.status
        if status_code == 18:
            return None, ValueError("The object of a GetParent request is itself the root of a content record tree")
        if status_code == 19:
            return None, ValueError("The object of a GetChildren request is itself a leaf of a content record tree")
        if status_code != 0:
            raise RuntimeError("Unsuccessful Request")
        return response_reader, None

    @staticmethod
    def validate_doi(doi: Union[str, AssetDoitype]) -> AssetDoitype:
        """
        Validate the DOI and convert it to an AssetDoitype.

        Parameters:
            doi (Union[str, AssetDoitype]): The DOI to validate.

        Raises: Value Error If doi is Not a string or AssetDOIType

        Raises: Value Error if doi is None/Empty

        Returns:
            AssetDoitype: The validated DOI.
        """
        if isinstance(doi, str):
            doi_string = doi
        elif isinstance(doi, AssetDoitype):
            doi_string = doi.value
        else:
            raise ValueError("DOI Must Be String")
        if len(doi_string) <= 0:
            raise ValueError("DOI Cannot Be Empty Or None")
        return AssetDoitype(doi_string)

    def serialize(self, req) -> str:
        """
        Serialize the given Request object into an XML string using the configured serializer.

        Parameters:
            req (Request): The Request object to serialize.

        Returns:
            str: The serialized XML representation of the request.
        """

        return self.serializer.render(req, self.ns_map)
