from dataclasses import dataclass, field
from typing import Optional

from scheme.org.eidr.schema.doi_mode_restricted import DoiModeRestricted
from scheme.org.eidr.schema.language_track_type_type import (
    LanguageTrackTypeType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class LanguageType:
    class Meta:
        name = "languageType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    mode: Optional[DoiModeRestricted] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    type_value: Optional[LanguageTrackTypeType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
