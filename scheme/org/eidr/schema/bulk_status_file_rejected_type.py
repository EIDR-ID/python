from dataclasses import dataclass, field
from typing import Optional

from scheme.org.eidr.schema.bulk_status_file_rejected_type_status import (
    BulkStatusFileRejectedTypeStatus,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class BulkStatusFileRejectedType:
    class Meta:
        name = "bulkStatusFileRejectedType"

    detail: Optional[str] = field(
        default=None,
        metadata={
            "name": "Detail",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    status: Optional[BulkStatusFileRejectedTypeStatus] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
