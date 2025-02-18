from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from scheme.com.movielabs.schema.md.v2.pkg_8.md.digital_asset_watermark_type import (
    DigitalAssetWatermarkType,
)
from scheme.com.movielabs.schema.md.v2.pkg_8.md.string_audio_enc_channel_mapping import (
    StringAudioEncChannelMapping,
)
from scheme.com.movielabs.schema.md.v2.pkg_8.md.string_audio_enc_codec import (
    StringAudioEncCodec,
)
from scheme.com.movielabs.schema.md.v2.pkg_8.md.string_audio_enc_vbr import (
    StringAudioEncVbr,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class DigitalAssetAudioEncodingType:
    class Meta:
        name = "DigitalAssetAudioEncoding-type"

    codec: Optional[StringAudioEncCodec] = field(
        default=None,
        metadata={
            "name": "Codec",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
    codec_type: list[str] = field(
        default_factory=list,
        metadata={
            "name": "CodecType",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "pattern": r"(mpeg4ra|IANA|rfc4281):.{1,128}",
        },
    )
    bitrate_max: Optional[int] = field(
        default=None,
        metadata={
            "name": "BitrateMax",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    bitrate_average: Optional[int] = field(
        default=None,
        metadata={
            "name": "BitrateAverage",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    vbr: Optional[StringAudioEncVbr] = field(
        default=None,
        metadata={
            "name": "VBR",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    sample_rate: Optional[int] = field(
        default=None,
        metadata={
            "name": "SampleRate",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    sample_bit_depth: Optional[int] = field(
        default=None,
        metadata={
            "name": "SampleBitDepth",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    channel_mapping: Optional[StringAudioEncChannelMapping] = field(
        default=None,
        metadata={
            "name": "ChannelMapping",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    watermark: list[DigitalAssetWatermarkType] = field(
        default_factory=list,
        metadata={
            "name": "Watermark",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    actual_length: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ActualLength",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
