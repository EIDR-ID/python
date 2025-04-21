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
from app.scheme.org.eidr.schema.graph.get_remotest_ancestor_type import GetRemotestAncestorType
from app.scheme.org.eidr.schema.graph.get_lightweight_relationships_type import GetLightweightRelationshipsType
from app.scheme.org.eidr.schema.graph.get_children_type import GetChildrenType
from app.scheme.org.eidr.schema.graph.get_parent_type import GetParentType
from app.scheme.org.eidr.schema.graph.get_series_ancestry_type import GetSeriesAncestryType
from app.scheme.org.eidr.schema.graph.get_leaf_descendants_type import GetLeafDescendantsType

from app.scheme.org.eidr.schema.request import Request
from app.scheme.org.eidr.schema.asset_doitype import AssetDoitype
import app.driver as Driver
import app.services.response_reader as ResponseReader
from requests import Response

from typing import Tuple
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
# <Response_Reader xmlns="http://www.eidr.org/schema" version="2.0.9">
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
# </Response_Reader>
class GraphTraversal():
    """
    A class to handle graph traversal operations for a given DOI.
    """

    def __init__(self, driver: 'Driver.API_Driver'):
        self.driver = driver
        self.doi = None
        self.name = "object/graph"
        self.serializer = XmlSerializer(config=SerializerConfig(indent="    "))
        self.ns_map = {"": "http://www.eidr.org/schema"}

    def find_ancestors(
            self,
            doi: Optional[Union[str, AssetDoitype]] = None,
            referent_type_filter: list[ReferentType] = None,
            relationship_type_filter: list[RelationshipType] = None,
            structural_type_filter: list[CreationStructuralType] = None,
            find_ancestors: FindAncestorsType = None,
    ) -> Tuple[Optional['ResponseReader.ResponseReader'], Optional[ValueError]]:
        """
        Retrieve the ancestors of a given DOI.
        Parameters:
            doi (Optional[Union[str, AssetDoitype]]): The DOI to search for. If not provided, it will be validated.
            referent_type_filter (list[ReferentType]): A list of referent types to filter by.
            relationship_type_filter (list[RelationshipType]): A list of relationship types to filter by.
            structural_type_filter (list[CreationStructuralType]): A list of structural types to filter by.
            find_ancestors (FindAncestorsType): An instance of FindAncestorsType containing the search criteria.
        Returns:
            Tuple[Optional[ResponseReader], Optional[ValueError]]:
                A tuple where the first element is the ResponseReader instance
                containing relationship data, and the second is an optional ValueError
                indicating any issues with the response status code.
        """
        if doi is None:
            doi = self.validate_doi(self.doi)
        else:
            doi = self.validate_doi(doi)

        find_ancestors = FindAncestorsType(
            id=doi,
            referent_type=referent_type_filter,
            relationship_type=relationship_type_filter,
            structural_type=structural_type_filter,
        )
        self.validate_doi(find_ancestors.id)
        operation = OperationType(find_ancestors=find_ancestors)
        return self.validate_response(self.create_operations([operation]))

    def get_remotest_ancestor(
            self,
            doi: Optional[Union[str, AssetDoitype]] = None,
    ) -> Tuple[Optional['ResponseReader.ResponseReader'], Optional[ValueError]]:
        """
        Retrieves remotest ancestor of a Digital Object
        Returns:
            Tuple[Optional[ResponseReader], Optional[ValueError]]:
                A tuple where the first element is the ResponseReader instance
                containing relationship data, and the second is an optional ValueError
                indicating any issues with the response status code.
        """
        if doi is None:
            doi = self.validate_doi(self.doi)
        else:
            doi = self.validate_doi(doi)

        get_remotest = GetRemotestAncestorType(id=doi)
        operation = OperationType(get_remotest_ancestor=get_remotest)
        return self.validate_response(self.create_operations([operation]))

    def find_descendants(
            self,
            doi: Optional[Union[str, AssetDoitype]] = None,
            extended_family: Optional[bool] = False,
            referent_type_filter: list[ReferentType] = None,
            relationship_type_filter: list[RelationshipType] = None,
            structural_type_filter: list[CreationStructuralType] = None,
    ) -> Tuple[Optional['ResponseReader.ResponseReader'], Optional[ValueError]]:
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
                Tuple[Optional[ResponseReader], Optional[ValueError]]:
                    A tuple where the first element is the ResponseReader instance
                    containing relationship data, and the second is an optional ValueError
                    indicating any issues with the response status code.   str: The serialized XML representation of the request.
        """
        if doi is None:
            doi = self.validate_doi(self.doi)
        else:
            doi = self.validate_doi(doi)

        find_descendants = FindDescendantsType(
            id=doi,
            extended_family=extended_family,
            referent_type=referent_type_filter,
            relationship_type=relationship_type_filter,
            structural_type=structural_type_filter,
        )
        operation = OperationType(find_descendants=find_descendants)
        return self.validate_response(self.create_operations([operation]))

    def get_leaf_descendants(
            self,
            doi: Optional[Union[str, AssetDoitype]] = None
    ) -> Tuple[Optional['ResponseReader.ResponseReader'], Optional[ValueError]]:
        """
        Retrieve the leaf descendants of a given DOI.
        Returns:
            Tuple[Optional[ResponseReader], Optional[ValueError]]:
                A tuple where the first element is the ResponseReader instance
                containing relationship data, and the second is an optional ValueError
                indicating any issues with the response status code.

        """
        if doi is None:
            doi = self.validate_doi(self.doi)
        else:
            doi = self.validate_doi(doi)

        leaf_descendant = GetLeafDescendantsType(id=doi)
        operation = OperationType(get_leaf_descendants=leaf_descendant)
        return self.validate_response(self.create_operations([operation]))

    def get_lightweight_relationships(
            self,
            doi: Optional[Union[str, AssetDoitype]] = None
    ) -> Tuple[Optional['ResponseReader.ResponseReader'], Optional[ValueError]]:
        """
                Retrieves lightweight relationships of a Digital Object.

        Returns:
            Tuple[Optional[ResponseReader], Optional[ValueError]]:
                A tuple where the first element is the ResponseReader instance
                containing relationship data, and the second is an optional ValueError
                indicating any issues with the response status code.

        """
        if doi is None:
            doi = self.validate_doi(self.doi)
        else:
            doi = self.validate_doi(doi)

        light_weight = GetLightweightRelationshipsType(id=doi)
        operation = OperationType(get_lightweight_relationships=light_weight)
        return self.validate_response(self.create_operations([operation]))

    def get_dependants(
            self,
            doi: Optional[Union[str, AssetDoitype]] = None
    ) -> Tuple[Optional['ResponseReader.ResponseReader'], Optional[ValueError]]:
        """
        Retrieves all dependents of a Digital Object.

        Returns:
            Tuple[Optional[ResponseReader], Optional[ValueError]]:
                A tuple where the first element is the ResponseReader instance
                containing dependent objects, and the second is an optional ValueError
                indicating any issues with the response status code.

        Notes:
            - Dependants are objects upon which the given object depends.
        """
        if doi is None:
            doi = self.validate_doi(self.doi)
        else:
            doi = self.validate_doi(doi)

        get_dependants = GetDependantsType(id=doi)
        operation = OperationType(get_dependents=get_dependants)
        return self.validate_response(self.create_operations([operation]))

    def get_children(
            self,
            doi: Optional[Union[str, AssetDoitype]] = None
    ) -> Tuple[Optional['ResponseReader.ResponseReader'], Optional[ValueError]]:
        """
        Retrieves immediate dependents (children) of a Digital Object.

        Returns:
            Tuple[Optional[ResponseReader], Optional[ValueError]]:
                A tuple where the first element is the ResponseReader instance
                containing child objects, and the second is an optional ValueError
                indicating any issues with the response status code.

        Notes:
            - Children are direct dependents in the object's dependency tree.
        """
        if doi is None:
            doi = self.validate_doi(self.doi)
        else:
            doi = self.validate_doi(doi)

        children = GetChildrenType(id=doi)
        operation = OperationType(get_children=children)
        return self.validate_response(self.create_operations([operation]))

    def get_parent(
            self,
            doi: Optional[Union[str, AssetDoitype]] = None
    ) -> Tuple[Optional['ResponseReader.ResponseReader'], Optional[ValueError]]:
        """
        Retrieves the immediate ancestor (parent) of a Digital Object.

        Returns:
            Tuple[Optional[ResponseReader], Optional[ValueError]]:
                A tuple where the first element is the ResponseReader instance
                containing parent information, and the second is an optional ValueError
                indicating any issues with the response status code.

        Notes:
            - The parent is the direct ancestor in the object's lineage.
        """
        if doi is None:
            doi = self.validate_doi(self.doi)
        else:
            doi = self.validate_doi(doi)

        parent = GetParentType(id=doi)
        operation = OperationType(get_parent=parent)
        return self.validate_response(self.create_operations([operation]))

    def get_series_ancestry(
            self,
            doi: Optional[Union[str, AssetDoitype]] = None
    ) -> Tuple[Optional['ResponseReader.ResponseReader'], Optional[ValueError]]:
        """
            Retrieves all ancestors of a Digital Object, tracing its lineage.

            Returns:
                Tuple[Optional[ResponseReader], Optional[ValueError]]:
                    A tuple where the first element is the ResponseReader instance
                    containing ancestor information, and the second is an optional ValueError
                    indicating any issues with the response status code.

            Notes:
                - Series ancestry provides a complete lineage of the object.
    """
        if doi is None:
            doi = self.validate_doi(self.doi)
        else:
            doi = self.validate_doi(doi)

        series = GetSeriesAncestryType(id=doi)
        operation = OperationType(get_series_ancestry=series)
        return self.validate_response(self.create_operations([operation]))

    def video_service_get_children(
            self,
            doi: Optional[Union[str, AssetDoitype]] = None,
            all_children: bool = False
    ) -> Tuple[Optional['ResponseReader.ResponseReader'], Optional[ValueError]]:
        """
        Retrieves the children of a given Digital Object using the video service.

        Parameters:
            doi (Optional[Union[str, AssetDoitype]]): The DOI to search for. If not provided, it will be validated.
            all_children (bool): Whether to include all children in the result.

        Returns:
            Tuple[Optional[ResponseReader.ResponseReader], Optional[ValueError]]:
                A tuple where the first element is the ResponseReader instance
                containing child information, and the second is an optional ValueError
                indicating any issues with the response status code.
    """
        if doi is None:
            doi = self.validate_doi(self.doi)
        else:
            doi = self.validate_doi(doi)

        response = self.driver.get_video_service_traversal(
            service_doi=doi,
            service_endpoint="children",
            all_children=all_children
        )
        return self.validate_response(response=response)

    def video_service_get_parent(
            self,
            doi: Optional[Union[str, AssetDoitype]] = None
    ) -> Tuple[Optional['ResponseReader.ResponseReader'], Optional[ValueError]]:
        """
        Retrieves the parent of a given Digital Object using the video service.

        Parameters:
            doi (Optional[Union[str, AssetDoitype]]): The DOI to search for. If not provided, it will be validated.

        Returns:
            Tuple[Optional[ResponseReader.ResponseReader], Optional[ValueError]]:
                A tuple where the first element is the ResponseReader instance
                containing parent information, and the second is an optional ValueError
                indicating any issues with the response status code.
        """
        if doi is None:
            doi = self.validate_doi(self.doi)
        else:
            doi = self.validate_doi(doi)

        response = self.driver.get_video_service_traversal(
            service_doi=doi,
            service_endpoint="parent",
            all_children=False
        )
        return self.validate_response(response=response)

    def validate_response(
            self,
            request: Request= None,
            response: Response = None,
    ) -> Tuple[Optional['ResponseReader.ResponseReader'], Optional[ValueError]]:
        """
            Validates and processes the response from a server request.
            validates response if request is not provided
        Args:
            request (Request): The request object to be sent.

        Returns:
            Tuple[Optional[ResponseReader], Optional[ValueError]]:
                A tuple containing the ResponseReader instance if successful,
                or None if an error occurs. The second element is a ValueError
                if there's an issue with the response status code.

        Notes:
            - Sends the request using POST.
            - Converts the response content to pretty-formatted XML.
            - Uses ResponseReader to parse the XML and check the status code.
            - Raises specific errors based on status codes 18 and 19.
        """
        if response is None:
            response = self.driver.post_raw(
                self.serialize(request),
                self.name
            )

        response.raise_for_status()
        xml = Driver.to_pretty_xml(response.content)
        response_reader: ResponseReader = ResponseReader.ResponseReader(res_str=xml, driver=self.driver)
        status_code, _ = response_reader.status
        if status_code == 18:
            return None, ValueError("The object of a GetParent request is itself the root of a content record tree", {response_reader.status})
        if status_code == 19:
            return None, ValueError("The object of a GetChildren request is itself a leaf of a content record tree", {response_reader.status})
        if status_code != 0:
            return None, ValueError("Unsuccessful Request", f"Status Code: {response_reader.status}")
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
