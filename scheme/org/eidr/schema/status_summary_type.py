from dataclasses import dataclass, field

from scheme.org.eidr.schema.status_list_element_type import (
    StatusListElementType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class StatusSummaryType:
    class Meta:
        name = "statusSummaryType"

    status_summary_item: list[StatusListElementType] = field(
        default_factory=list,
        metadata={
            "name": "StatusSummaryItem",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "max_occurs": 6,
        },
    )
