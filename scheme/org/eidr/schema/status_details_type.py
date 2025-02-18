from dataclasses import dataclass, field
from typing import Optional

from scheme.org.eidr.schema.status_code_type import StatusCodeType
from scheme.org.eidr.schema.status_type_type import StatusTypeType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class StatusDetailsType:
    class Meta:
        name = "statusDetailsType"

    code: Optional[StatusCodeType] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    type_value: Optional[StatusTypeType] = field(
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
