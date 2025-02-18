from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class UsageDetailsType:
    class Meta:
        name = "usageDetailsType"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 128,
        },
    )
    domain: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 256,
            "pattern": r"[\S]+[.][\S]+",
        },
    )
