from dataclasses import dataclass

from scheme.org.eidr.schema.all_inherited_info_type import AllInheritedInfoType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class InheritedMetadata(AllInheritedInfoType):
    class Meta:
        namespace = "http://www.eidr.org/schema"
