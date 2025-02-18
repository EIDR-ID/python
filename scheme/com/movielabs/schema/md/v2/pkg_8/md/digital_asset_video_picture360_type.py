from dataclasses import dataclass, field
from typing import Optional

from scheme.com.movielabs.schema.md.v2.pkg_8.md.digital_asset_video_picture360_initial_type import (
    DigitalAssetVideoPicture360InitialType,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class DigitalAssetVideoPicture360Type:
    class Meta:
        name = "DigitalAssetVideoPicture360-type"

    projection: Optional[str] = field(
        default=None,
        metadata={
            "name": "Projection",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
    rendering: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rendering",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    initial_view: Optional[DigitalAssetVideoPicture360InitialType] = field(
        default=None,
        metadata={
            "name": "InitialView",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
