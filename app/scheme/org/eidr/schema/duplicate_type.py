from dataclasses import dataclass, field
from typing import Optional

from    .asset_doitype import AssetDoitype

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class DuplicateType:
    """This element captures the IDs of the duplicates.

    Textual details about the reason for identifying as a duplicate may
    optionally be returned.
    """

    class Meta:
        name = "duplicateType"

    id: Optional[AssetDoitype] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    details: Optional[str] = field(
        default=None,
        metadata={
            "name": "Details",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "max_length": 256,
        },
    )
    score: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 100,
        },
    )
    low_threshold: Optional[int] = field(
        default=None,
        metadata={
            "name": "lowThreshold",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 100,
        },
    )
    high_threshold: Optional[int] = field(
        default=None,
        metadata={
            "name": "highThreshold",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 100,
        },
    )
