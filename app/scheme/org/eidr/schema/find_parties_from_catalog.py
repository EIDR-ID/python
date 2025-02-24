from dataclasses import dataclass

from    .party_query_type import PartyQueryType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class FindPartiesFromCatalog(PartyQueryType):
    class Meta:
        namespace = "http://www.eidr.org/schema"
