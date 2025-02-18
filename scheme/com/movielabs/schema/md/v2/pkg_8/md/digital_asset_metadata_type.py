from dataclasses import dataclass, field
from typing import Optional

from scheme.com.movielabs.schema.md.v2.pkg_8.md.digital_asset_audio_data_type import (
    DigitalAssetAudioDataType,
)
from scheme.com.movielabs.schema.md.v2.pkg_8.md.digital_asset_interactive_data_type import (
    DigitalAssetInteractiveDataType,
)
from scheme.com.movielabs.schema.md.v2.pkg_8.md.digital_asset_subtitle_data_type import (
    DigitalAssetSubtitleDataType,
)
from scheme.com.movielabs.schema.md.v2.pkg_8.md.digital_asset_video_data_type import (
    DigitalAssetVideoDataType,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class DigitalAssetMetadataType:
    class Meta:
        name = "DigitalAssetMetadata-type"

    audio: Optional[DigitalAssetAudioDataType] = field(
        default=None,
        metadata={
            "name": "Audio",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    video: Optional[DigitalAssetVideoDataType] = field(
        default=None,
        metadata={
            "name": "Video",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    subtitle: Optional[DigitalAssetSubtitleDataType] = field(
        default=None,
        metadata={
            "name": "Subtitle",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    interactive: Optional[DigitalAssetInteractiveDataType] = field(
        default=None,
        metadata={
            "name": "Interactive",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
