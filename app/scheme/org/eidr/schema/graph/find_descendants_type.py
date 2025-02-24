from dataclasses import dataclass, field
from typing import Optional

from app.scheme.org.doi.pkg_2010.doischema_avs.creation_structural_type import (
    CreationStructuralType,
)
from    app.scheme.org.eidr.schema.asset_doitype import AssetDoitype
from    app.scheme.org.eidr.schema.referent_type import ReferentType
from    app.scheme.org.eidr.schema.relationship_type import RelationshipType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class FindDescendantsType:

    class Meta:
        name = "findDescendantsType"

    id: Optional[AssetDoitype] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    referent_type: list[ReferentType] = field(
        default_factory=list,
        metadata={
            "name": "ReferentType",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "max_occurs": 8,
        },
    )
    structural_type: list[CreationStructuralType] = field(
        default_factory=list,
        metadata={
            "name": "StructuralType",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "max_occurs": 5,
        },
    )
    relationship_type: list[RelationshipType] = field(
        default_factory=list,
        metadata={
            "name": "RelationshipType",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "max_occurs": 12,
        },
    )
    extended_family: Optional[bool] = field(
        default=None,
        metadata={
            "name": "extendedFamily",
            "type": "Attribute",
        },
    )
