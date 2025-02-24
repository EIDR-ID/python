from dataclasses import dataclass, field
from typing import Optional

from    .party_resolution_type import PartyResolutionType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class PartyQueryResultsType:
    class Meta:
        name = "partyQueryResultsType"

    current_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "CurrentSize",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    total_matches: Optional[int] = field(
        default=None,
        metadata={
            "name": "TotalMatches",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    continuation_token: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContinuationToken",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    party_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "PartyID",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "pattern": r"10\.5237/[0-9a-fA-F]{4}-[0-9a-fA-F]{4}|10\.5237/superparty",
        },
    )
    party: list[PartyResolutionType] = field(
        default_factory=list,
        metadata={
            "name": "Party",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
