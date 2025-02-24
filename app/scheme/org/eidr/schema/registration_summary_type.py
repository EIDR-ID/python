from dataclasses import dataclass, field

from    .report_creation_list_element_type import (
    ReportCreationListElementType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class RegistrationSummaryType:
    class Meta:
        name = "registrationSummaryType"

    registration_summary_item: list[ReportCreationListElementType] = field(
        default_factory=list,
        metadata={
            "name": "RegistrationSummaryItem",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "max_occurs": 12,
        },
    )
