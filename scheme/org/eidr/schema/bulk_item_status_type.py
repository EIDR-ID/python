from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from scheme.org.eidr.schema.bulk_item_info_type import BulkItemInfoType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class BulkItemStatusType:
    class Meta:
        name = "bulkItemStatusType"

    local_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocalID",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
            "pattern": r"LOCAL:[0-9a-zA-Z_#/\.\-\(\)]{1,128}",
        },
    )
    last_updated: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LastUpdated",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    info: Optional[BulkItemInfoType] = field(
        default=None,
        metadata={
            "name": "Info",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
