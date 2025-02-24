from dataclasses import dataclass, field

from    .party_query_type import PartyQueryType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class FindPartiesByName(PartyQueryType):
    class Meta:
        namespace = "http://www.eidr.org/schema"

    include_alternate_names: bool = field(
        default=False,
        metadata={
            "name": "includeAlternateNames",
            "type": "Attribute",
        },
    )
