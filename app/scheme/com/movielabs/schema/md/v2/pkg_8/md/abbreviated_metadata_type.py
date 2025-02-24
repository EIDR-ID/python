from dataclasses import dataclass, field
from typing import Optional

from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.abbreviated_metadata_info_type import (
    AbbreviatedMetadataInfoType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.content_identifier_type import (
    ContentIdentifierType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.content_rating_type import (
    ContentRatingType,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class AbbreviatedMetadataType:
    """
    :ivar update_num:
    :ivar localized_info:
    :ivar rating:
    :ivar alt_identifier:
    :ivar studio: Equivalent to DisplayName
    :ivar content_id:
    """

    class Meta:
        name = "AbbreviatedMetadata-type"

    update_num: Optional[int] = field(
        default=None,
        metadata={
            "name": "UpdateNum",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "min_inclusive": 1,
        },
    )
    localized_info: list[AbbreviatedMetadataInfoType] = field(
        default_factory=list,
        metadata={
            "name": "LocalizedInfo",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "min_occurs": 1,
        },
    )
    rating: list[ContentRatingType] = field(
        default_factory=list,
        metadata={
            "name": "Rating",
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
    studio: Optional[str] = field(
        default=None,
        metadata={
            "name": "Studio",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
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
