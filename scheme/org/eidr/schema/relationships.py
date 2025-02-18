from dataclasses import dataclass

from scheme.org.eidr.schema.relationships_info_type import (
    RelationshipsInfoType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class Relationships(RelationshipsInfoType):
    class Meta:
        namespace = "http://www.eidr.org/schema"
