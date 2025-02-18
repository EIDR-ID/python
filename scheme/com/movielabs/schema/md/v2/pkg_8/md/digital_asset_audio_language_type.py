from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class DigitalAssetAudioLanguageType:
    class Meta:
        name = "DigitalAssetAudioLanguage-type"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    dubbed: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
