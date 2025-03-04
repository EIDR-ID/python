from typing import Optional, Union

from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from app.scheme.org.eidr.schema import ReferentType, RelationshipType
from app.scheme.org.eidr.schema.operation_type import OperationType

# from    .graph.find_descendants_type import FindDescendantsType
## this is the correct Import the one above is broken fix imports
from app.scheme.org.eidr.schema.graph.find_descendants_type import FindDescendantsType
from app.scheme.org.eidr.schema.graph.find_ancestors_type import FindAncestorsType
from app.scheme.org.eidr.schema.graph.get_dependants_type import GetDependantsType
from app.scheme.org.eidr.schema.request import Request
from app.scheme.org.eidr.schema.asset_doitype import AssetDoitype
import app.driver as Driver
import  app.services.res as ResponseReader
from requests import Response

from typing import  Tuple
from app.scheme.org.doi.pkg_2010.doischema_avs.creation_structural_type import (
    CreationStructuralType,
)


# Example Of Graph Request
# <Request xmlns="http://www.eidr.org/schema"
#     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
#     <Operation>
#         <GetRemotestAncestor>
#             <ID>10.5240/8B55-F9AA-007F-B18E-C000-6</ID>
#         </GetRemotestAncestor>
#     </Operation>
# </Request>


# <?xml version="1.0" encoding="UTF-8"?>
# <Response xmlns="http://www.eidr.org/schema" version="2.0.9">
#     <Status><Code>0</Code><Type>success</Type></Status>
#     <SimpleMetadata>
#         <ID>10.5240/FB0D-0A93-CAD6-8E8D-80C2-4</ID>
#         <StructuralType>Abstraction</StructuralType>
#         <ReferentType>Movie</ReferentType>
#         <ResourceName titleClass="release" lang="en">Gone with the
#         Wind</ResourceName>
#         <OriginalLanguage mode="Audio" type="primary">en</OriginalLanguage>
#         <ReleaseDate>1939-12-15</ReleaseDate>
#         <Status>valid</Status>
# </SimpleMetadata>
# <GenerationsAbove>1</GenerationsAbove>
# </Response>
class GraphTraversal:
    """
    A class to handle graph traversal operations for a given DOI.
    """

    def __init__(self, driver: Driver.API_Driver):
        self.driver = driver
        self.doi = None
        self.name = "object/graph"
        self.serializer = XmlSerializer(config=SerializerConfig(indent="    "))
        self.ns_map = {"": "http://www.eidr.org/schema"}

    def find_ancestors(
            self,
            referent_type_filter: list[ReferentType] = None,
            relationship_type_filter: list[RelationshipType] = None,
            structural_type_filter: list[CreationStructuralType] = None,
            find_ancestors: FindAncestorsType = None,
    ) -> Tuple[ResponseReader,ValueError]:
        """
        Retrieve the ancestors of a given DOI.

        Parameters:
            doi (Optional[Union[str, AssetDoitype]]): The DOI to search for. If not provided, it will be validated.
            referent_type_filter (list[ReferentType]): A list of referent types to filter by.
            relationship_type_filter (list[RelationshipType]): A list of relationship types to filter by.
            structural_type_filter (list[CreationStructuralType]): A list of structural types to filter by.
            find_ancestors (FindAncestorsType): An instance of FindAncestorsType containing the search criteria.

        Returns:
            str: The serialized XML representation of the request.
        """
        if find_ancestors is None:
            doi = self.validate_doi(self.doi)
            find_ancestors = FindAncestorsType(
                id=doi,
                referent_type=referent_type_filter,
                relationship_type=relationship_type_filter,
                structural_type=structural_type_filter,
            )
        self.validate_doi(find_ancestors.id)
        operation = OperationType(find_ancestors=find_ancestors)
        return self.validate_response(self.create_operations([operation]))

    def validate_response(self, request: Request) -> (ResponseReader, ValueError):
        response = self.driver.post_raw(
            self.serialize(request),
            self.name
        )
        response.raise_for_status()
        xml = Driver.to_pretty_xml(response.content)
        response_reader: ResponseReader = ResponseReader.ResponseReader(xml)
        status_code, _ = response_reader.status
        if status_code == 18:
            return None, ValueError("The object of a GetParent request is itself the root of a content record tree")
        if status_code == 19:
            return None,ValueError("The object of a GetChildren request is itself a leaf of a content record tree")
        if status_code != 0:
            raise RuntimeError("Unsuccessful Request")
        return response_reader,None

    def find_descendants(
            self,
            doi: Optional[Union[str, AssetDoitype]] = None,
            extended_family: Optional[bool] = False,
            referent_type_filter: list[ReferentType] = None,
            relationship_type_filter: list[RelationshipType] = None,
            structural_type_filter: list[CreationStructuralType] = None,
            find_descendants: FindDescendantsType = None,
    ) -> str:
        """
        Retrieve the descendants of a given DOI.

        Parameters:
            doi (Optional[Union[str, AssetDoitype]]): The DOI to search for. If not provided, it will be validated.
            extended_family (Optional[bool]): Whether to include extended family members in the result.
            referent_type_filter (list[ReferentType]): A list of referent types to filter by.
            relationship_type_filter (list[RelationshipType]): A list of relationship types to filter by.
            structural_type_filter (list[CreationStructuralType]): A list of structural types to filter by.
            find_descendants (FindDescendantsType): An instance of FindDescendantsType containing the search criteria.

        Returns:
            str: The serialized XML representation of the request.
        """
        if find_descendants is None:
            doi = self.validate_doi(doi)
            find_descendants = FindDescendantsType(
                id=doi,
                extended_family=extended_family,
                referent_type=referent_type_filter,
                relationship_type=relationship_type_filter,
                structural_type=structural_type_filter,
            )
        self.validate_doi(find_descendants.id)
        operation = OperationType(find_descendants=find_descendants)
        req = self.create_operations([operation])
        return self.serialize(req)

    def get_dependants(
            self,
            doi: Optional[Union[str, AssetDoitype]] = None,
            get_dependants: GetDependantsType = None,
    ) -> str:
        """
        Retrieve the dependants of a given DOI.

        Parameters:
            doi (Optional[Union[str, AssetDoitype]]): The DOI to search for. If not provided, it will be validated.
            get_dependants (GetDependantsType): An instance of GetDependantsType containing the search criteria.

        Returns:
            str: The serialized XML representation of the request.
        """
        if get_dependants is None:
            doi = self.validate_doi(doi)
            get_dependants = GetDependantsType(id=doi)
        self.validate_doi(get_dependants.id)
        operation = OperationType(get_dependents=get_dependants)
        req = self.create_operations([operation])
        return self.serialize(req)

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

    @staticmethod
    def create_operations(operation: list[OperationType]) -> Request:
        """
        Create a Request object from a list of OperationType objects.

        Parameters:
            operation (list[OperationType]): A list of OperationType objects to include in the request.

        Returns:
            Request: The created Request object.
        """
        return Request(operation=operation)

    def serialize(self, req) -> str:
        """
        Serialize the given Request object into an XML string using the configured serializer.

        Parameters:
            req (Request): The Request object to serialize.

        Returns:
            str: The serialized XML representation of the request.
        """

        return self.serializer.render(req, self.ns_map)
