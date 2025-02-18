from dataclasses import dataclass

from scheme.org.eidr.schema.party_alias_continuation_type import (
    PartyAliasContinuationType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class PartyAliasContinuation(PartyAliasContinuationType):
    class Meta:
        namespace = "http://www.eidr.org/schema"
