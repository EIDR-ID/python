from dataclasses import dataclass, field
from typing import Optional

from scheme.com.movielabs.schema.md.v2.pkg_8.md.digital_asset_color_volume_type import (
    DigitalAssetColorVolumeType,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class DigitalAssetColorTransformMetadataType:
    class Meta:
        name = "DigitalAssetColorTransformMetadata-type"

    color_volume_transform: Optional[str] = field(
        default=None,
        metadata={
            "name": "ColorVolumeTransform",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
    application_identifier: Optional[
        "DigitalAssetColorTransformMetadataType.ApplicationIdentifier"
    ] = field(
        default=None,
        metadata={
            "name": "ApplicationIdentifier",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    target_system_display: Optional[DigitalAssetColorVolumeType] = field(
        default=None,
        metadata={
            "name": "TargetSystemDisplay",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    do_not_transcode_base: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DoNotTranscodeBase",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )

    @dataclass
    class ApplicationIdentifier:
        value: Optional[int] = field(
            default=None,
            metadata={
                "required": True,
            },
        )
        application_version: Optional[int] = field(
            default=None,
            metadata={
                "name": "applicationVersion",
                "type": "Attribute",
            },
        )
