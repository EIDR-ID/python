from dataclasses import dataclass

from    .simple_info_type import SimpleInfoType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class SimpleInfo(SimpleInfoType):
    class Meta:
        namespace = "http://www.eidr.org/schema"
