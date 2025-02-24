from dataclasses import dataclass

from    .party_doilist_type import PartyDoilistType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class PartyIdlist(PartyDoilistType):
    class Meta:
        name = "PartyIDList"
        namespace = "http://www.eidr.org/schema"
