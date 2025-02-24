from dataclasses import dataclass, field
from typing import Optional

from scheme.org.eidr.schema.asset_doitype import AssetDoitype

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class GetDependantsType:
    class Meta:
        name = "getDependantsType"


    id: Optional[AssetDoitype] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
