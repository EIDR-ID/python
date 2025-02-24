from dataclasses import dataclass, field
from typing import Optional

from    .asset_doitype import AssetDoitype

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class VirtualFieldsType:
    class Meta:
        name = "virtualFieldsType"

    id: Optional[AssetDoitype] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    full: Optional[str] = field(
        default=None,
        metadata={
            "name": "Full",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    self_defined: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelfDefined",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    alias: Optional[str] = field(
        default=None,
        metadata={
            "name": "Alias",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
