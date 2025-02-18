from dataclasses import dataclass, field
from typing import Optional

from scheme.org.eidr.schema.title_class_type import TitleClassType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class TitleType:
    class Meta:
        name = "titleType"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 256,
        },
    )
    title_class: Optional[TitleClassType] = field(
        default=None,
        metadata={
            "name": "titleClass",
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    system_generated: Optional[bool] = field(
        default=None,
        metadata={
            "name": "systemGenerated",
            "type": "Attribute",
        },
    )
