from dataclasses import dataclass, field
from typing import Optional

from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.digital_asset_video_picture_frame_rate_type import (
    DigitalAssetVideoPictureFrameRateType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.digital_asset_video_picture_progressive_type import (
    DigitalAssetVideoPictureProgressiveType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.string_video_pic_color_sampling import (
    StringVideoPicColorSampling,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.string_video_pic_colorimetry import (
    StringVideoPicColorimetry,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.string_video_pic_pixel_aspect import (
    StringVideoPicPixelAspect,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.string_video_pic_type3_d import (
    StringVideoPicType3D,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class DigitalAssetVideoPictureType:
    """
    Redefine to require AspectRatio.
    """

    class Meta:
        name = "DigitalAssetVideoPicture-type"

    aspect_ratio: Optional[str] = field(
        default=None,
        metadata={
            "name": "AspectRatio",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
            "pattern": r"[0-9]{1,2}:[0-9]|([0-9]\.[0-9][0-9]):[0-9]",
        },
    )
    pixel_aspect: Optional[StringVideoPicPixelAspect] = field(
        default=None,
        metadata={
            "name": "PixelAspect",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    width_pixels: Optional[int] = field(
        default=None,
        metadata={
            "name": "WidthPixels",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    height_pixels: Optional[int] = field(
        default=None,
        metadata={
            "name": "HeightPixels",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    active_width_pixels: Optional[int] = field(
        default=None,
        metadata={
            "name": "ActiveWidthPixels",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    active_height_pixels: Optional[int] = field(
        default=None,
        metadata={
            "name": "ActiveHeightPixels",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
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
    color_subsampling: Optional[StringVideoPicColorSampling] = field(
        default=None,
        metadata={
            "name": "ColorSubsampling",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    colorimetry: Optional[StringVideoPicColorimetry] = field(
        default=None,
        metadata={
            "name": "Colorimetry",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    type3_d: Optional[StringVideoPicType3D] = field(
        default=None,
        metadata={
            "name": "Type3D",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
