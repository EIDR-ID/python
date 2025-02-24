from dataclasses import dataclass, field
from typing import Optional

from    .asset_doitype import AssetDoitype

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class GetLightweightRelationshipsType:
    class Meta:
        name = "getLightweightRelationshipsType"

    id: Optional[AssetDoitype] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
