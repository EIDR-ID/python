from dataclasses import dataclass

from scheme.org.eidr.schema.alternate_ids_type import AlternateIdsType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class AlternateIds(AlternateIdsType):
    class Meta:
        name = "AlternateIDs"
        namespace = "http://www.eidr.org/schema"
