from dataclasses import dataclass, field
from typing import Optional

from scheme.org.eidr.schema.asset_doitype import AssetDoitype
from scheme.org.eidr.schema.target_relationship_type import (
    TargetRelationshipType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class RemoveRelationshipType:
    class Meta:
        name = "removeRelationshipType"

    id: Optional[AssetDoitype] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    target_id: Optional[AssetDoitype] = field(
        default=None,
        metadata={
            "name": "TargetID",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    type_value: Optional[TargetRelationshipType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )
