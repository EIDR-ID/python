from dataclasses import dataclass

from    .party_creation_type import PartyCreationType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class CreateParty(PartyCreationType):
    class Meta:
        namespace = "http://www.eidr.org/schema"
