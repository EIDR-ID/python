from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class DescriptionType:
    class Meta:
        name = "descriptionType"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 128,
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
