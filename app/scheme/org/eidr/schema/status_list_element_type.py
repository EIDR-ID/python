from dataclasses import dataclass, field
from typing import Optional

from    .operation_status_code_type import (
    OperationStatusCodeType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class StatusListElementType:
    class Meta:
        name = "statusListElementType"

    code: Optional[OperationStatusCodeType] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    count: Optional[int] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
