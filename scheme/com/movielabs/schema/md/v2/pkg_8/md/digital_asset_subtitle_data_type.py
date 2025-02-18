from dataclasses import dataclass, field
from typing import Optional

from scheme.com.movielabs.schema.md.v2.pkg_8.md.digital_asset_cardset_list_type import (
    DigitalAssetCardsetListType,
)
from scheme.com.movielabs.schema.md.v2.pkg_8.md.digital_asset_subtitle_format_type import (
    DigitalAssetSubtitleFormatType,
)
from scheme.com.movielabs.schema.md.v2.pkg_8.md.private_data_type import (
    PrivateDataType,
)
from scheme.com.movielabs.schema.md.v2.pkg_8.md.string_subtitle_format_type import (
    StringSubtitleFormatType,
)
from scheme.com.movielabs.schema.md.v2.pkg_8.md.string_subtitle_type import (
    StringSubtitleType,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class DigitalAssetSubtitleDataType:
    class Meta:
        name = "DigitalAssetSubtitleData-type"

    format: Optional[DigitalAssetSubtitleFormatType] = field(
        default=None,
        metadata={
            "name": "Format",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "max_length": 128,
        },
    )
    type_value: list[StringSubtitleType] = field(
        default_factory=list,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "min_occurs": 1,
            "max_occurs": 8,
        },
    )
    format_type: Optional[StringSubtitleFormatType] = field(
        default=None,
        metadata={
            "name": "FormatType",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
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
