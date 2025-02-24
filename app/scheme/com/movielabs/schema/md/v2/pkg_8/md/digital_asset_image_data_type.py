from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.compliance_type import (
    ComplianceType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.content_identifier_type import (
    ContentIdentifierType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.digital_asset_video_picture_type import (
    DigitalAssetVideoPictureType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.private_data_type import (
    PrivateDataType,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class DigitalAssetImageDataType:
    class Meta:
        name = "DigitalAssetImageData-type"

    description: list["DigitalAssetImageDataType.Description"] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    type_value: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    sub_type: list[str] = field(
        default_factory=list,
        metadata={
            "name": "SubType",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    purpose: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Purpose",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    width: Optional[int] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
    height: Optional[int] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
    encoding: Optional[str] = field(
        default=None,
        metadata={
            "name": "Encoding",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
    picture_details: Optional[DigitalAssetVideoPictureType] = field(
        default=None,
        metadata={
            "name": "PictureDetails",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    dynamic_range_profile: Optional[
        "DigitalAssetImageDataType.DynamicRangeProfile"
    ] = field(
        default=None,
        metadata={
            "name": "DynamicRangeProfile",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    color_gamut_profile: Optional[str] = field(
        default=None,
        metadata={
            "name": "ColorGamutProfile",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    language: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    compliance: list[ComplianceType] = field(
        default_factory=list,
        metadata={
            "name": "Compliance",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    track_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrackReference",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "max_length": 128,
        },
    )
    track_identifier: list[ContentIdentifierType] = field(
        default_factory=list,
        metadata={
            "name": "TrackIdentifier",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    private: Optional[PrivateDataType] = field(
        default=None,
        metadata={
            "name": "Private",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )

    @dataclass
    class Description:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        language: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class DynamicRangeProfile:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        luminance_min: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "LuminanceMin",
                "type": "Attribute",
            },
        )
        luminance_max: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "LuminanceMax",
                "type": "Attribute",
            },
        )
