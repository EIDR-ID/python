from dataclasses import dataclass

from    .all_self_defined_info_type import (
    AllSelfDefinedInfoType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class SelfDefinedMetadata(AllSelfDefinedInfoType):
    class Meta:
        namespace = "http://www.eidr.org/schema"
