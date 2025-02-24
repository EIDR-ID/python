from dataclasses import dataclass, field
from typing import Optional

from    .service_resolution_type import (
    ServiceResolutionType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class ServiceQueryResultsType:
    class Meta:
        name = "serviceQueryResultsType"

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
    service: list[ServiceResolutionType] = field(
        default_factory=list,
        metadata={
            "name": "Service",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
