from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class PartyAliasContinuationType:
    class Meta:
        name = "partyAliasContinuationType"

    last_aliased: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastAliased",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
            "pattern": r"10\.5237/[0-9a-fA-F]{4}-[0-9a-fA-F]{4}|10\.5237/superparty",
        },
    )
    target_of_last_aliased: Optional[str] = field(
        default=None,
        metadata={
            "name": "TargetOfLastAliased",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
            "pattern": r"10\.5237/[0-9a-fA-F]{4}-[0-9a-fA-F]{4}|10\.5237/superparty",
        },
    )
