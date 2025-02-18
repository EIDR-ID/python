from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class AltServiceNameType:
    class Meta:
        name = "altServiceNameType"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 128,
        },
    )
    abbreviation: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
