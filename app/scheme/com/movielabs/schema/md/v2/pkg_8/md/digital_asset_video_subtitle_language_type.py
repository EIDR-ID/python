from dataclasses import dataclass, field
from typing import Optional

from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.string_video_sub_lang_type import (
    StringVideoSubLangType,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class DigitalAssetVideoSubtitleLanguageType:
    class Meta:
        name = "DigitalAssetVideoSubtitleLanguage-type"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    closed: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    type_value: Optional[StringVideoSubLangType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
