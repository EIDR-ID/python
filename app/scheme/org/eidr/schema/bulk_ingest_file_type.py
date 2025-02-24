from dataclasses import dataclass, field
from typing import Optional

from    .bulk_item_type import BulkItemType
from    .registrant_type import RegistrantType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class BulkIngestFileType:
    class Meta:
        name = "bulkIngestFileType"

    filename: Optional[str] = field(
        default=None,
        metadata={
            "name": "Filename",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
            "max_length": 64,
        },
    )
    registrant: Optional[RegistrantType] = field(
        default=None,
        metadata={
            "name": "Registrant",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    num_items: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumItems",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    item: list[BulkItemType] = field(
        default_factory=list,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "min_occurs": 1,
            "max_occurs": 5000,
        },
    )
