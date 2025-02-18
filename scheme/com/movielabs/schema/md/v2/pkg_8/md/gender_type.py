from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class GenderType:
    class Meta:
        name = "Gender-type"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    transgender: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_gender: Optional[str] = field(
        default=None,
        metadata={
            "name": "specificGender",
            "type": "Attribute",
        },
    )
