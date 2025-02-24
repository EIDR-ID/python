from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from    .operation_status_type_type import (
    OperationStatusTypeType,
)
from    .registrant_type import RegistrantType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class RequestStatusType:
    class Meta:
        name = "requestStatusType"

    token: Optional[str] = field(
        default=None,
        metadata={
            "name": "Token",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    user_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "UserID",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "pattern": r"10\.5238/[0-9a-zA-Z_#\.\-\(\)]{3,32}",
        },
    )
    registrant: Optional[RegistrantType] = field(
        default=None,
        metadata={
            "name": "Registrant",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    status: Optional[OperationStatusTypeType] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    from_value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "From",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    to: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "To",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    after: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "After",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    page_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "PageNumber",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    page_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "PageSize",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
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
