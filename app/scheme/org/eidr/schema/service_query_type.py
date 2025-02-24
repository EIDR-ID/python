from dataclasses import dataclass, field
from typing import Optional

from    .active_filter_type import ActiveFilterType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class ServiceQueryType:
    class Meta:
        name = "serviceQueryType"

    service_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceName",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    active_filter: ActiveFilterType = field(
        default=ActiveFilterType.ALL,
        metadata={
            "name": "ActiveFilter",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    page_number: int = field(
        default=1,
        metadata={
            "name": "PageNumber",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    page_size: int = field(
        default=20,
        metadata={
            "name": "PageSize",
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
