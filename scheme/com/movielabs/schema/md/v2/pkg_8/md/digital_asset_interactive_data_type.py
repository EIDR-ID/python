from dataclasses import dataclass, field
from typing import Optional

from scheme.com.movielabs.schema.md.v2.pkg_8.md.digital_asset_interactive_encoding_type import (
    DigitalAssetInteractiveEncodingType,
)
from scheme.com.movielabs.schema.md.v2.pkg_8.md.private_data_type import (
    PrivateDataType,
)
from scheme.com.movielabs.schema.md.v2.pkg_8.md.string_interactive_format_type import (
    StringInteractiveFormatType,
)
from scheme.com.movielabs.schema.md.v2.pkg_8.md.string_interactive_type import (
    StringInteractiveType,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class DigitalAssetInteractiveDataType:
    class Meta:
        name = "DigitalAssetInteractiveData-type"

    type_value: Optional[StringInteractiveType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
    format_type: Optional[StringInteractiveFormatType] = field(
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
        },
    )
    encoding: list[DigitalAssetInteractiveEncodingType] = field(
        default_factory=list,
        metadata={
            "name": "Encoding",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "min_occurs": 1,
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
