from dataclasses import dataclass

from scheme.org.eidr.schema.linked_alternate_ids_type import (
    LinkedAlternateIdsType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class LinkedAlternateIds(LinkedAlternateIdsType):
    class Meta:
        name = "LinkedAlternateIDs"
        namespace = "http://www.eidr.org/schema"
