from dataclasses import dataclass, field
from typing import Optional

from    .asset_doitype import AssetDoitype

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class AliasType:
    class Meta:
        name = "aliasType"

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
            "required": True,
        },
    )
