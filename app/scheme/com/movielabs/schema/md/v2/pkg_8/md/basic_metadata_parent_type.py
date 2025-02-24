from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlDuration, XmlPeriod

from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.associated_org_type import (
    AssociatedOrgType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.basic_metadata_info_type import (
    BasicMetadataInfoType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.basic_metadata_parent_type_relationship_type import (
    BasicMetadataParentTypeRelationshipType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.basic_metadata_people_type import (
    BasicMetadataPeopleType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.color_type_type import (
    ColorTypeType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.content_identifier_type import (
    ContentIdentifierType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.content_rating_type import (
    ContentRatingType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.content_related_to_type import (
    ContentRelatedToType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.content_sequence_info_type import (
    ContentSequenceInfoType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.region_type import RegionType
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.release_history_type import (
    ReleaseHistoryType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.version_intent_type import (
    VersionIntentType,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class BasicMetadataParentType:
    class Meta:
        name = "BasicMetadataParent-type"

    parent_content_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParentContentID",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "pattern": r"10\.5240/[\dA-F]{4}-[\dA-F]{4}-[\dA-F]{4}-[\dA-F]{4}-[\dA-F]{4}-[\dA-Z]|10\.5240/[\dA-F]{20}[\dA-Z]",
        },
    )
    parent: Optional["BasicMetadataType"] = field(
        default=None,
        metadata={
            "name": "Parent",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    sequence_info: Optional[ContentSequenceInfoType] = field(
        default=None,
        metadata={
            "name": "SequenceInfo",
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
    excluded_region: list[RegionType] = field(
        default_factory=list,
        metadata={
            "name": "ExcludedRegion",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    relationship_type: Optional[BasicMetadataParentTypeRelationshipType] = (
        field(
            default=None,
            metadata={
                "name": "relationshipType",
                "type": "Attribute",
            },
        )
    )


@dataclass
class BasicMetadataType:
    class Meta:
        name = "BasicMetadata-type"

    update_num: Optional[int] = field(
        default=None,
        metadata={
            "name": "UpdateNum",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "min_inclusive": 1,
        },
    )
    localized_info: list[BasicMetadataInfoType] = field(
        default_factory=list,
        metadata={
            "name": "LocalizedInfo",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "min_occurs": 1,
        },
    )
    run_length: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "RunLength",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    release_year: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "ReleaseYear",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
    release_date: Optional[Union[XmlPeriod, XmlDate, XmlDateTime]] = field(
        default=None,
        metadata={
            "name": "ReleaseDate",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    release_history: list[ReleaseHistoryType] = field(
        default_factory=list,
        metadata={
            "name": "ReleaseHistory",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    work_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "WorkType",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
    work_type_detail: list[str] = field(
        default_factory=list,
        metadata={
            "name": "WorkTypeDetail",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    picture_color_type: Optional[ColorTypeType] = field(
        default=None,
        metadata={
            "name": "PictureColorType",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    picture_format: Optional[str] = field(
        default=None,
        metadata={
            "name": "PictureFormat",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    three_d: Optional["BasicMetadataType.ThreeD"] = field(
        default=None,
        metadata={
            "name": "ThreeD",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    aspect_ratio: Optional[str] = field(
        default=None,
        metadata={
            "name": "AspectRatio",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    alt_identifier: list[ContentIdentifierType] = field(
        default_factory=list,
        metadata={
            "name": "AltIdentifier",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    rating_set: Optional[ContentRatingType] = field(
        default=None,
        metadata={
            "name": "RatingSet",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    people: list[BasicMetadataPeopleType] = field(
        default_factory=list,
        metadata={
            "name": "People",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    country_of_origin: list[RegionType] = field(
        default_factory=list,
        metadata={
            "name": "CountryOfOrigin",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    primary_spoken_language: list[str] = field(
        default_factory=list,
        metadata={
            "name": "PrimarySpokenLanguage",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    original_language: list[str] = field(
        default_factory=list,
        metadata={
            "name": "OriginalLanguage",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    version_language: list[str] = field(
        default_factory=list,
        metadata={
            "name": "VersionLanguage",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    version_intent: Optional[VersionIntentType] = field(
        default=None,
        metadata={
            "name": "VersionIntent",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    associated_org: list[AssociatedOrgType] = field(
        default_factory=list,
        metadata={
            "name": "AssociatedOrg",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    content_related_to: list[ContentRelatedToType] = field(
        default_factory=list,
        metadata={
            "name": "ContentRelatedTo",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    sequence_info: Optional[ContentSequenceInfoType] = field(
        default=None,
        metadata={
            "name": "SequenceInfo",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    parent: list[BasicMetadataParentType] = field(
        default_factory=list,
        metadata={
            "name": "Parent",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    content_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContentID",
            "type": "Attribute",
            "required": True,
            "pattern": r"10\.5240/[\dA-F]{4}-[\dA-F]{4}-[\dA-F]{4}-[\dA-F]{4}-[\dA-F]{4}-[\dA-Z]|10\.5240/[\dA-F]{20}[\dA-Z]",
        },
    )

    @dataclass
    class ThreeD:
        value: Optional[bool] = field(
            default=None,
            metadata={
                "required": True,
            },
        )
        three60: Optional[bool] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        multiview: Optional[bool] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
