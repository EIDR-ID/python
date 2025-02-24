from dataclasses import dataclass, field

from    .relationship_info_type import RelationshipInfoType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class RelationshipsInfoType:
    class Meta:
        name = "relationshipsInfoType"

    relationship: list[RelationshipInfoType] = field(
        default_factory=list,
        metadata={
            "name": "Relationship",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
