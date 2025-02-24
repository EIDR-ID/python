from dataclasses import dataclass, field
from typing import Optional

from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.color_type_type import (
    ColorTypeType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.digital_asset_cardset_list_type import (
    DigitalAssetCardsetListType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.digital_asset_video_encoding_type import (
    DigitalAssetVideoEncodingType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.digital_asset_video_picture_type import (
    DigitalAssetVideoPictureType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.digital_asset_video_subtitle_language_type import (
    DigitalAssetVideoSubtitleLanguageType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.private_data_type import (
    PrivateDataType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.string_video_picture_format import (
    StringVideoPictureFormat,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.string_video_type import (
    StringVideoType,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class DigitalAssetVideoDataType:
    """
    :ivar description:
    :ivar type_value:
    :ivar encoding:
    :ivar picture:
    :ivar color_type: BW, Color, Colorized, etc.
    :ivar picture_format:
    :ivar subtitle_language:
    :ivar signed_language:
    :ivar cardset_list:
    :ivar track_reference:
    :ivar private:
    """

    class Meta:
        name = "DigitalAssetVideoData-type"

    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "max_length": 128,
        },
    )
    type_value: Optional[StringVideoType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    encoding: Optional[DigitalAssetVideoEncodingType] = field(
        default=None,
        metadata={
            "name": "Encoding",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    picture: Optional[DigitalAssetVideoPictureType] = field(
        default=None,
        metadata={
            "name": "Picture",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
    color_type: Optional[ColorTypeType] = field(
        default=None,
        metadata={
            "name": "ColorType",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    picture_format: Optional[StringVideoPictureFormat] = field(
        default=None,
        metadata={
            "name": "PictureFormat",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    subtitle_language: list[DigitalAssetVideoSubtitleLanguageType] = field(
        default_factory=list,
        metadata={
            "name": "SubtitleLanguage",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    signed_language: Optional[str] = field(
        default=None,
        metadata={
            "name": "SignedLanguage",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    cardset_list: list[DigitalAssetCardsetListType] = field(
        default_factory=list,
        metadata={
            "name": "CardsetList",
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
    private: Optional[PrivateDataType] = field(
        default=None,
        metadata={
            "name": "Private",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
