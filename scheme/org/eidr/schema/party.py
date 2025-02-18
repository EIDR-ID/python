from dataclasses import dataclass

from scheme.org.eidr.schema.party_resolution_type import PartyResolutionType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class Party(PartyResolutionType):
    class Meta:
        namespace = "http://www.eidr.org/schema"
