from dataclasses import dataclass

from    .provenance_info_type import ProvenanceInfoType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class ProvenanceMetadata(ProvenanceInfoType):
    class Meta:
        namespace = "http://www.eidr.org/schema"
