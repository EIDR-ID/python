from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from scheme.com.movielabs.schema.md.v2.pkg_8.md.digital_asset_chromaticity_type import (
    DigitalAssetChromaticityType,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class DigitalAssetColorVolumeType:
    class Meta:
        name = "DigitalAssetColorVolume-type"

    primary_rchromaticity: Optional[DigitalAssetChromaticityType] = field(
        default=None,
        metadata={
            "name": "PrimaryRChromaticity",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
    primary_gchromaticity: Optional[DigitalAssetChromaticityType] = field(
        default=None,
        metadata={
            "name": "PrimaryGChromaticity",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
    primary_bchromaticity: Optional[DigitalAssetChromaticityType] = field(
        default=None,
        metadata={
            "name": "PrimaryBChromaticity",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
    white_point_chromaticity: Optional[DigitalAssetChromaticityType] = field(
        default=None,
        metadata={
            "name": "WhitePointChromaticity",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
    luminance_min: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "LuminanceMin",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
    luminance_max: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "LuminanceMax",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
