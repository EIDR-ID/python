from dataclasses import dataclass, field
from typing import Optional

from scheme.com.movielabs.schema.md.v2.pkg_8.md.string_video_pic_frame_rate_multiplier import (
    StringVideoPicFrameRateMultiplier,
)
from scheme.com.movielabs.schema.md.v2.pkg_8.md.string_video_pic_frame_rate_timecode import (
    StringVideoPicFrameRateTimecode,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class DigitalAssetVideoPictureFrameRateType:
    class Meta:
        name = "DigitalAssetVideoPictureFrameRate-type"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    multiplier: Optional[StringVideoPicFrameRateMultiplier] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    timecode: Optional[StringVideoPicFrameRateTimecode] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
