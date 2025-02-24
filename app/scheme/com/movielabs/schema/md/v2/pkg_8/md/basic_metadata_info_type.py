from dataclasses import dataclass, field
from typing import Optional

from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.audience_type import (
    AudienceType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.basic_metadata_people_type import (
    BasicMetadataPeopleType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.region_type import RegionType

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class BasicMetadataInfoType:
    class Meta:
        name = "BasicMetadataInfo-type"

    title_display19: Optional[str] = field(
        default=None,
        metadata={
            "name": "TitleDisplay19",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    title_display60: Optional[str] = field(
        default=None,
        metadata={
            "name": "TitleDisplay60",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    title_display_unlimited: Optional[str] = field(
        default=None,
        metadata={
            "name": "TitleDisplayUnlimited",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    title_sort: Optional[str] = field(
        default=None,
        metadata={
            "name": "TitleSort",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    art_reference: list["BasicMetadataInfoType.ArtReference"] = field(
        default_factory=list,
        metadata={
            "name": "ArtReference",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    summary190: Optional["BasicMetadataInfoType.Summary190"] = field(
        default=None,
        metadata={
            "name": "Summary190",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    summary400: Optional["BasicMetadataInfoType.Summary400"] = field(
        default=None,
        metadata={
            "name": "Summary400",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    summary4000: Optional["BasicMetadataInfoType.Summary4000"] = field(
        default=None,
        metadata={
            "name": "Summary4000",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    display_indicators: list[str] = field(
        default_factory=list,
        metadata={
            "name": "DisplayIndicators",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    genre: list["BasicMetadataInfoType.Genre"] = field(
        default_factory=list,
        metadata={
            "name": "Genre",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    keyword: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Keyword",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    version_notes: Optional[str] = field(
        default=None,
        metadata={
            "name": "VersionNotes",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    region: list[RegionType] = field(
        default_factory=list,
        metadata={
            "name": "Region",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    target_audience: list[AudienceType] = field(
        default_factory=list,
        metadata={
            "name": "TargetAudience",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    original_title: Optional[str] = field(
        default=None,
        metadata={
            "name": "OriginalTitle",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    copyright_line: Optional[str] = field(
        default=None,
        metadata={
            "name": "CopyrightLine",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    people_local: list[BasicMetadataPeopleType] = field(
        default_factory=list,
        metadata={
            "name": "PeopleLocal",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    title_alternate: list["BasicMetadataInfoType.TitleAlternate"] = field(
        default_factory=list,
        metadata={
            "name": "TitleAlternate",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
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
    condition: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class ArtReference:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        resolution: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        purpose: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Summary190:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        cast: Optional[bool] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Summary400:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        cast: Optional[bool] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Summary4000:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        cast: Optional[bool] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Genre:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        source: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        level: Optional[int] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class TitleAlternate:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        type_value: Optional[str] = field(
            default=None,
            metadata={
                "name": "type",
                "type": "Attribute",
            },
        )
        language: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
