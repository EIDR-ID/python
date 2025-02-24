from dataclasses import dataclass, field
from typing import Optional

from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.content_related_to_character_type import (
    ContentRelatedToCharacterType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.content_related_to_event_type import (
    ContentRelatedToEventType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.content_related_to_period_type import (
    ContentRelatedToPeriodType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.content_related_to_person_type import (
    ContentRelatedToPersonType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.content_related_to_place_type import (
    ContentRelatedToPlaceType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.content_related_to_relationship_type import (
    ContentRelatedToRelationshipType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.content_related_to_work_type import (
    ContentRelatedToWorkType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.grouping_entity_type import (
    GroupingEntityType,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class ContentRelatedToType:
    """
    :ivar relationship: Describes how the original people place or
        things are modified.  These can be controleld vocaublary or free
        text.
    :ivar description: Description of the subject of the work.
        Especially important if other elements are insuffiicent.
    :ivar work:
    :ivar character:
    :ivar person_or_group:
    :ivar period:
    :ivar place:
    :ivar event:
    :ivar grouping_entity:
    """

    class Meta:
        name = "ContentRelatedTo-type"

    relationship: Optional[ContentRelatedToRelationshipType] = field(
        default=None,
        metadata={
            "name": "Relationship",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
    description: list["ContentRelatedToType.Description"] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    work: list[ContentRelatedToWorkType] = field(
        default_factory=list,
        metadata={
            "name": "Work",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    character: list[ContentRelatedToCharacterType] = field(
        default_factory=list,
        metadata={
            "name": "Character",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    person_or_group: list[ContentRelatedToPersonType] = field(
        default_factory=list,
        metadata={
            "name": "PersonOrGroup",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    period: list[ContentRelatedToPeriodType] = field(
        default_factory=list,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    place: list[ContentRelatedToPlaceType] = field(
        default_factory=list,
        metadata={
            "name": "Place",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    event: list[ContentRelatedToEventType] = field(
        default_factory=list,
        metadata={
            "name": "Event",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    grouping_entity: list[GroupingEntityType] = field(
        default_factory=list,
        metadata={
            "name": "GroupingEntity",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )

    @dataclass
    class Description:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        language: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
