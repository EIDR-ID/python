from dataclasses import dataclass, field
from typing import Optional

from scheme.org.eidr.schema.asset_doitype import AssetDoitype

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class AliasContinuationType:
    class Meta:
        name = "aliasContinuationType"

    last_aliased: Optional[AssetDoitype] = field(
        default=None,
        metadata={
            "name": "LastAliased",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    target_of_last_aliased: Optional[AssetDoitype] = field(
        default=None,
        metadata={
            "name": "TargetOfLastAliased",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
