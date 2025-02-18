from dataclasses import dataclass, field
from typing import Optional

from scheme.com.movielabs.schema.md.v2.pkg_8.md.abbreviated_metadata_info_type_display_indicators import (
    AbbreviatedMetadataInfoTypeDisplayIndicators,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class AbbreviatedMetadataInfoType:
    class Meta:
        name = "AbbreviatedMetadataInfo-type"

    title_brief: Optional[str] = field(
        default=None,
        metadata={
            "name": "TitleBrief",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
    art_reference: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ArtReference",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    summary_short: Optional[str] = field(
        default=None,
        metadata={
            "name": "SummaryShort",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
    display_indicators: list[AbbreviatedMetadataInfoTypeDisplayIndicators] = (
        field(
            default_factory=list,
            metadata={
                "name": "DisplayIndicators",
                "type": "Element",
                "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            },
        )
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    default: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
