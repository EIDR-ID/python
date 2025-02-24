from dataclasses import dataclass

from   .all_inherited_info_type import AllInheritedInfoType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class ResolvedInheritedGeneral(AllInheritedInfoType):
    class Meta:
        namespace = "http://www.eidr.org/schema"
