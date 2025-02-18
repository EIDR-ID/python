from dataclasses import dataclass, field
from typing import Optional

from scheme.org.eidr.schema.batch_status_code_type import BatchStatusCodeType
from scheme.org.eidr.schema.batch_status_type_type import BatchStatusTypeType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class BatchStatusDetailsType:
    class Meta:
        name = "batchStatusDetailsType"

    code: Optional[BatchStatusCodeType] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    type_value: Optional[BatchStatusTypeType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
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
