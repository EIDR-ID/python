from dataclasses import dataclass, field
from typing import Optional

from scheme.org.eidr.schema.asset_doitype import AssetDoitype
from scheme.org.eidr.schema.supplemental_content_class_type import (
    SupplementalContentClassType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class SupplementalContentInfoType:
    class Meta:
        name = "supplementalContentInfoType"

    id: Optional[AssetDoitype] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    supplemental_content_class: Optional[SupplementalContentClassType] = field(
        default=None,
        metadata={
            "name": "SupplementalContentClass",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
