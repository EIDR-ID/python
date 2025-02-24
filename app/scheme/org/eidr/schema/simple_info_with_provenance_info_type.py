from dataclasses import dataclass, field
from typing import Optional

from    .provenance_info_type import ProvenanceInfoType
from    .simple_info_type import SimpleInfoType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class SimpleInfoWithProvenanceInfoType:
    class Meta:
        name = "simpleInfoWithProvenanceInfoType"

    simple_metadata: Optional[SimpleInfoType] = field(
        default=None,
        metadata={
            "name": "SimpleMetadata",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    provenance_metadata: Optional[ProvenanceInfoType] = field(
        default=None,
        metadata={
            "name": "ProvenanceMetadata",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
