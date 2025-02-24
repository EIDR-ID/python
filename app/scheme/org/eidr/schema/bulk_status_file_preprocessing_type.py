from dataclasses import dataclass, field
from typing import Optional

from    .bulk_status_file_preprocessing_type_status import (
    BulkStatusFilePreprocessingTypeStatus,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class BulkStatusFilePreprocessingType:
    class Meta:
        name = "bulkStatusFilePreprocessingType"

    detail: Optional[str] = field(
        default=None,
        metadata={
            "name": "Detail",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    status: Optional[BulkStatusFilePreprocessingTypeStatus] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
