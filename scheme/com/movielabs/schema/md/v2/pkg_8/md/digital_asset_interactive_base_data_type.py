from dataclasses import dataclass, field
from typing import Optional

from scheme.com.movielabs.schema.md.v2.pkg_8.md.string_interactive_format_type import (
    StringInteractiveFormatType,
)
from scheme.com.movielabs.schema.md.v2.pkg_8.md.string_interactive_type import (
    StringInteractiveType,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class DigitalAssetInteractiveBaseDataType:
    class Meta:
        name = "DigitalAssetInteractiveBaseData-type"

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
