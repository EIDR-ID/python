from dataclasses import dataclass, field
from typing import Optional

from    .operation_type import OperationType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class RequestType:
    class Meta:
        name = "requestType"

    operation: list[OperationType] = field(
        default_factory=list,
        metadata={
            "name": "Operation",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "min_occurs": 1,
            "max_occurs": 100,
        },
    )
    user_token: Optional[str] = field(
        default=None,
        metadata={
            "name": "userToken",
            "type": "Attribute",
        },
    )
