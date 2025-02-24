from dataclasses import dataclass, field
from typing import Optional

from    .report_creation_type import ReportCreationType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class ReportCreationListElementType:
    class Meta:
        name = "reportCreationListElementType"

    type_value: Optional[ReportCreationType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    count: Optional[int] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
