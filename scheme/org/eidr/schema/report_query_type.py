from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from scheme.org.doi.pkg_2010.doischema_avs.creation_structural_type import (
    CreationStructuralType,
)
from scheme.org.eidr.schema.referent_type import ReferentType
from scheme.org.eidr.schema.registrant_type import RegistrantType
from scheme.org.eidr.schema.relationship_type import RelationshipType
from scheme.org.eidr.schema.status_type import StatusType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class ReportQueryType:
    class Meta:
        name = "reportQueryType"

    from_value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "From",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    to: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "To",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    registrant: Optional[RegistrantType] = field(
        default=None,
        metadata={
            "name": "Registrant",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
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
    status: list[StatusType] = field(
        default_factory=list,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "max_occurs": 3,
        },
    )
