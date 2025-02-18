from dataclasses import dataclass, field
from typing import Optional

from scheme.org.eidr.schema.bulk_item_status_type import BulkItemStatusType
from scheme.org.eidr.schema.bulk_status_file_done_type_status import (
    BulkStatusFileDoneTypeStatus,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class BulkStatusFileDoneType:
    class Meta:
        name = "bulkStatusFileDoneType"

    detail: Optional[str] = field(
        default=None,
        metadata={
            "name": "Detail",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    item: list[BulkItemStatusType] = field(
        default_factory=list,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "max_occurs": 5000,
        },
    )
    status: Optional[BulkStatusFileDoneTypeStatus] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
