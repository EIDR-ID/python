from dataclasses import dataclass, field

from scheme.com.movielabs.schema.md.v2.pkg_8.md.digital_asset_ancillary_data_type import (
    DigitalAssetAncillaryDataType,
)
from scheme.com.movielabs.schema.md.v2.pkg_8.md.digital_asset_audio_data_type import (
    DigitalAssetAudioDataType,
)
from scheme.com.movielabs.schema.md.v2.pkg_8.md.digital_asset_image_data_type import (
    DigitalAssetImageDataType,
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
class DigitalAssetSetType:
    class Meta:
        name = "DigitalAssetSet-type"

    audio: list[DigitalAssetAudioDataType] = field(
        default_factory=list,
        metadata={
            "name": "Audio",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    video: list[DigitalAssetVideoDataType] = field(
        default_factory=list,
        metadata={
            "name": "Video",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    subtitle: list[DigitalAssetSubtitleDataType] = field(
        default_factory=list,
        metadata={
            "name": "Subtitle",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    image: list[DigitalAssetImageDataType] = field(
        default_factory=list,
        metadata={
            "name": "Image",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    interactive: list[DigitalAssetInteractiveDataType] = field(
        default_factory=list,
        metadata={
            "name": "Interactive",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    ancillary: list[DigitalAssetAncillaryDataType] = field(
        default_factory=list,
        metadata={
            "name": "Ancillary",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
