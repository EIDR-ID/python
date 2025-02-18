from dataclasses import dataclass, field
from typing import Optional

from scheme.org.eidr.schema.alternate_content_class_type import (
    AlternateContentClassType,
)
from scheme.org.eidr.schema.asset_doitype import AssetDoitype

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class AlternateContentInfoType:
    class Meta:
        name = "alternateContentInfoType"

    id: Optional[AssetDoitype] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    alternate_content_class: Optional[AlternateContentClassType] = field(
        default=None,
        metadata={
            "name": "AlternateContentClass",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
