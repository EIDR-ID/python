from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from    .bulk_status_file_done_type import (
    BulkStatusFileDoneType,
)
from    .bulk_status_file_preprocessing_type import (
    BulkStatusFilePreprocessingType,
)
from    .bulk_status_file_processing_type import (
    BulkStatusFileProcessingType,
)
from    .bulk_status_file_rejected_type import (
    BulkStatusFileRejectedType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class BulkStatusFileType:
    class Meta:
        name = "bulkStatusFileType"

    status_file: Optional[str] = field(
        default=None,
        metadata={
            "name": "StatusFile",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    original_file_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "OriginalFileName",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    started_processing: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StartedProcessing",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
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
    preprocessing: Optional[BulkStatusFilePreprocessingType] = field(
        default=None,
        metadata={
            "name": "Preprocessing",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    rejected: Optional[BulkStatusFileRejectedType] = field(
        default=None,
        metadata={
            "name": "Rejected",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    processing: Optional[BulkStatusFileProcessingType] = field(
        default=None,
        metadata={
            "name": "Processing",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    done: Optional[BulkStatusFileDoneType] = field(
        default=None,
        metadata={
            "name": "Done",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
