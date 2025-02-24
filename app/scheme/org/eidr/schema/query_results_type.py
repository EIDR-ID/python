from dataclasses import dataclass, field
from typing import Optional

from    .asset_doitype import AssetDoitype
from    .simple_info_type import SimpleInfoType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class QueryResultsType:
    class Meta:
        name = "queryResultsType"

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
    simple_metadata: list[SimpleInfoType] = field(
        default_factory=list,
        metadata={
            "name": "SimpleMetadata",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    id: list[AssetDoitype] = field(
        default_factory=list,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
