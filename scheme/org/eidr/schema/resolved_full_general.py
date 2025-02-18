from dataclasses import dataclass

from scheme.org.eidr.schema.full_object_info_type import FullObjectInfoType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class ResolvedFullGeneral(FullObjectInfoType):
    class Meta:
        namespace = "http://www.eidr.org/schema"
