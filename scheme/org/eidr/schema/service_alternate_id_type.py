from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class ServiceAlternateIdType:
    class Meta:
        name = "serviceAlternateIdType"

    value: str = field(
        default="",
        metadata={
            "required": True,
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
