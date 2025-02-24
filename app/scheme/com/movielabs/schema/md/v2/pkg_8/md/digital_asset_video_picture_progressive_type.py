from dataclasses import dataclass, field
from typing import Optional

from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.string_video_pic_progressive_scan_order import (
    StringVideoPicProgressiveScanOrder,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class DigitalAssetVideoPictureProgressiveType:
    class Meta:
        name = "DigitalAssetVideoPictureProgressive-type"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    scan_order: Optional[StringVideoPicProgressiveScanOrder] = field(
        default=None,
        metadata={
            "name": "scanOrder",
            "type": "Attribute",
        },
    )
