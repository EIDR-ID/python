from dataclasses import dataclass, field
from typing import Optional

from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.content_rating_detail_type import (
    ContentRatingDetailType,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class ContentRatingType:
    class Meta:
        name = "ContentRating-type"

    not_rated: Optional["ContentRatingType.NotRated"] = field(
        default=None,
        metadata={
            "name": "NotRated",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    rating: list[ContentRatingDetailType] = field(
        default_factory=list,
        metadata={
            "name": "Rating",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    adult_content: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AdultContent",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )

    @dataclass
    class NotRated:
        value: bool = field(
            init=False,
            default=True,
            metadata={
                "required": True,
            },
        )
        condition: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
