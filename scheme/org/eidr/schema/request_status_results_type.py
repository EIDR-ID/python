from dataclasses import dataclass, field
from typing import Optional

from scheme.org.eidr.schema.batch_status_details_type import (
    BatchStatusDetailsType,
)
from scheme.org.eidr.schema.operation_status_type import OperationStatusType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class RequestStatusResultsType:
    class Meta:
        name = "requestStatusResultsType"

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
    batch_status: Optional[BatchStatusDetailsType] = field(
        default=None,
        metadata={
            "name": "BatchStatus",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    operation_status: list[OperationStatusType] = field(
        default_factory=list,
        metadata={
            "name": "OperationStatus",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
