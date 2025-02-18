from dataclasses import dataclass, field
from typing import Optional

from scheme.org.eidr.schema.operation_status_code_type import (
    OperationStatusCodeType,
)
from scheme.org.eidr.schema.operation_status_type_type import (
    OperationStatusTypeType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class OperationStatusDetailsType:
    class Meta:
        name = "operationStatusDetailsType"

    code: Optional[OperationStatusCodeType] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    type_value: Optional[OperationStatusTypeType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    details_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "DetailsCode",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    details: Optional[str] = field(
        default=None,
        metadata={
            "name": "Details",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "max_length": 256,
        },
    )
