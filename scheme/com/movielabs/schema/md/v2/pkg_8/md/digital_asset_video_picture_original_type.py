from dataclasses import dataclass, field
from typing import Optional

from scheme.com.movielabs.schema.md.v2.pkg_8.md.digital_asset_video_picture_frame_rate_type import (
    DigitalAssetVideoPictureFrameRateType,
)
from scheme.com.movielabs.schema.md.v2.pkg_8.md.digital_asset_video_picture_progressive_type import (
    DigitalAssetVideoPictureProgressiveType,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class DigitalAssetVideoPictureOriginalType:
    class Meta:
        name = "DigitalAssetVideoPictureOriginal-type"

    frame_rate: Optional[DigitalAssetVideoPictureFrameRateType] = field(
        default=None,
        metadata={
            "name": "FrameRate",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    progressive: Optional[DigitalAssetVideoPictureProgressiveType] = field(
        default=None,
        metadata={
            "name": "Progressive",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
