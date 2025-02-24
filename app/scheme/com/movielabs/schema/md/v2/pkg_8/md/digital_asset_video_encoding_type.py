from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.digital_asset_watermark_type import (
    DigitalAssetWatermarkType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.string_video_enc_codec import (
    StringVideoEncCodec,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.string_video_enc_mlevel import (
    StringVideoEncMlevel,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.string_video_enc_mprofile import (
    StringVideoEncMprofile,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.string_video_enc_vbr import (
    StringVideoEncVbr,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class DigitalAssetVideoEncodingType:
    class Meta:
        name = "DigitalAssetVideoEncoding-type"

    codec: Optional[StringVideoEncCodec] = field(
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
            "pattern": r"(mpeg4ra|IANA):.{1,128}",
        },
    )
    mpegprofile: Optional[StringVideoEncMprofile] = field(
        default=None,
        metadata={
            "name": "MPEGProfile",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    mpeglevel: Optional[StringVideoEncMlevel] = field(
        default=None,
        metadata={
            "name": "MPEGLevel",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
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
    bit_rate_average: Optional[int] = field(
        default=None,
        metadata={
            "name": "BitRateAverage",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    vbr: Optional[StringVideoEncVbr] = field(
        default=None,
        metadata={
            "name": "VBR",
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
