from dataclasses import dataclass, field
from typing import Optional

from scheme.com.movielabs.schema.md.v2.pkg_8.md.gender_type import GenderType
from scheme.com.movielabs.schema.md.v2.pkg_8.md.grouping_entity_type import (
    GroupingEntityType,
)
from scheme.com.movielabs.schema.md.v2.pkg_8.md.person_identifier_type import (
    PersonIdentifierType,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class BasicMetadataCharacterType:
    class Meta:
        name = "BasicMetadataCharacter-type"

    character_name: list["BasicMetadataCharacterType.CharacterName"] = field(
        default_factory=list,
        metadata={
            "name": "CharacterName",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "min_occurs": 1,
        },
    )
    character_id: list[PersonIdentifierType] = field(
        default_factory=list,
        metadata={
            "name": "CharacterID",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    nonfictional: Optional["BasicMetadataCharacterType.Nonfictional"] = field(
        default=None,
        metadata={
            "name": "Nonfictional",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    gender: list[GenderType] = field(
        default_factory=list,
        metadata={
            "name": "Gender",
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
    sequence: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class CharacterName:
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

    @dataclass
    class Nonfictional:
        value: Optional[bool] = field(
            default=None,
            metadata={
                "required": True,
            },
        )
        appearance: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
