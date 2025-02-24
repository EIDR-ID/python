from dataclasses import dataclass, field
from typing import Optional

from scheme.org.eidr.schema.add_relationship_type import AddRelationshipType
from scheme.org.eidr.schema.alias_type import AliasType
from scheme.org.eidr.schema.create_type import CreateType
from scheme.org.eidr.schema.dedup_mode_type import DedupModeType
from scheme.org.eidr.schema.delete_type import DeleteType
from org.eidr.schema.graph.find_ancestors_type import FindAncestorsType
from org.eidr.schema.graph.find_descendants_type import FindDescendantsType
from org.eidr.schema.graph.get_children_type import GetChildrenType
from org.eidr.schema.graph.get_dependants_type import GetDependantsType
from org.eidr.schema.graph.get_leaf_descendants_type import (
    GetLeafDescendantsType,
)
from org.eidr.schema.get_lightweight_relationships_type import (
    GetLightweightRelationshipsType,
)
from org.eidr.schema.graph.get_parent_type import GetParentType
from org.eidr.schema.graph.get_remotest_ancestor_type import (
    GetRemotestAncestorType,
)
from org.eidr.schema.graph.get_series_ancestry_type import (
    GetSeriesAncestryType,
)
from scheme.org.eidr.schema.modify_type import ModifyType
from scheme.org.eidr.schema.promote_type import PromoteType
from scheme.org.eidr.schema.query_type import QueryType
from scheme.org.eidr.schema.remove_relationship_type import (
    RemoveRelationshipType,
)
from scheme.org.eidr.schema.replace_relationship_type import (
    ReplaceRelationshipType,
)
from scheme.org.eidr.schema.request_status_type import RequestStatusType
from scheme.org.eidr.schema.token_cancellation_request_type import (
    TokenCancellationRequestType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class OperationType:
    class Meta:
        name = "operationType"

    create: Optional[CreateType] = field(
        default=None,
        metadata={
            "name": "Create",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    add_relationship: Optional[AddRelationshipType] = field(
        default=None,
        metadata={
            "name": "AddRelationship",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    remove_relationship: Optional[RemoveRelationshipType] = field(
        default=None,
        metadata={
            "name": "RemoveRelationship",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    replace_relationship: Optional[ReplaceRelationshipType] = field(
        default=None,
        metadata={
            "name": "ReplaceRelationship",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    modify: Optional[ModifyType] = field(
        default=None,
        metadata={
            "name": "Modify",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    delete: Optional[DeleteType] = field(
        default=None,
        metadata={
            "name": "Delete",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    alias: Optional[AliasType] = field(
        default=None,
        metadata={
            "name": "Alias",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    promote: Optional[PromoteType] = field(
        default=None,
        metadata={
            "name": "Promote",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    find_ancestors: Optional[FindAncestorsType] = field(
        default=None,
        metadata={
            "name": "FindAncestors",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    find_descendants: Optional[FindDescendantsType] = field(
        default=None,
        metadata={
            "name": "FindDescendants",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    get_dependents: Optional[GetDependantsType] = field(
        default=None,
        metadata={
            "name": "GetDependents",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    get_series_ancestry: Optional[GetSeriesAncestryType] = field(
        default=None,
        metadata={
            "name": "GetSeriesAncestry",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    get_lightweight_relationships: Optional[
        GetLightweightRelationshipsType
    ] = field(
        default=None,
        metadata={
            "name": "GetLightweightRelationships",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    get_remotest_ancestor: Optional[GetRemotestAncestorType] = field(
        default=None,
        metadata={
            "name": "GetRemotestAncestor",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    get_leaf_descendants: Optional[GetLeafDescendantsType] = field(
        default=None,
        metadata={
            "name": "GetLeafDescendants",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    get_parent: Optional[GetParentType] = field(
        default=None,
        metadata={
            "name": "GetParent",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    get_children: Optional[GetChildrenType] = field(
        default=None,
        metadata={
            "name": "GetChildren",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    query: Optional[QueryType] = field(
        default=None,
        metadata={
            "name": "Query",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    status_request: Optional[RequestStatusType] = field(
        default=None,
        metadata={
            "name": "StatusRequest",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    token_cancellation_request: Optional[TokenCancellationRequestType] = field(
        default=None,
        metadata={
            "name": "TokenCancellationRequest",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    user_token: Optional[str] = field(
        default=None,
        metadata={
            "name": "userToken",
            "type": "Attribute",
        },
    )
    override: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dedup_mode: Optional[DedupModeType] = field(
        default=None,
        metadata={
            "name": "dedupMode",
            "type": "Attribute",
        },
    )
