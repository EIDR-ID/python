from dataclasses import dataclass, field

from    .simple_info_with_provenance_info_type import (
    SimpleInfoWithProvenanceInfoType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class RegistrationsType:
    class Meta:
        name = "registrationsType"

    registration: list[SimpleInfoWithProvenanceInfoType] = field(
        default_factory=list,
        metadata={
            "name": "Registration",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
