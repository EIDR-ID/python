from dataclasses import dataclass, field
from typing import Optional

from scheme.org.eidr.schema.asset_doitype import AssetDoitype
from scheme.org.eidr.schema.packaging_class_type import PackagingClassType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class PackagingInfoType:
    class Meta:
        name = "packagingInfoType"

    id: Optional[AssetDoitype] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    packaging_class: Optional[PackagingClassType] = field(
        default=None,
        metadata={
            "name": "PackagingClass",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
