from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class PartyDoilistType:
    class Meta:
        name = "partyDOIListType"

    party_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "PartyID",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "pattern": r"10\.5237/[0-9a-fA-F]{4}-[0-9a-fA-F]{4}|10\.5237/superparty",
        },
    )
