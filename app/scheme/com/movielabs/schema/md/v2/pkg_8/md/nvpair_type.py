from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class NvpairType:
    class Meta:
        name = "NVPair-type"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
