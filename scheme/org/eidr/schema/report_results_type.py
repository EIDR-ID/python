from dataclasses import dataclass, field
from typing import Optional

from scheme.org.eidr.schema.registration_summary_type import (
    RegistrationSummaryType,
)
from scheme.org.eidr.schema.registrations_type import RegistrationsType
from scheme.org.eidr.schema.status_summary_type import StatusSummaryType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class ReportResultsType:
    class Meta:
        name = "reportResultsType"

    status_summary: Optional[StatusSummaryType] = field(
        default=None,
        metadata={
            "name": "StatusSummary",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    registration_summary: Optional[RegistrationSummaryType] = field(
        default=None,
        metadata={
            "name": "RegistrationSummary",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    registrations: Optional[RegistrationsType] = field(
        default=None,
        metadata={
            "name": "Registrations",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
