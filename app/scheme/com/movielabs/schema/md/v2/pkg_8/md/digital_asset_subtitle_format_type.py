from dataclasses import dataclass, field
from typing import Optional

from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.string_subtitle_format import (
    StringSubtitleFormat,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class DigitalAssetSubtitleFormatType:
    class Meta:
        name = "DigitalAssetSubtitleFormat-type"

    value: Optional[StringSubtitleFormat] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    sdimage: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SDImage",
            "type": "Attribute",
        },
    )
    hdimage: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HDImage",
            "type": "Attribute",
        },
    )
