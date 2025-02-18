from dataclasses import dataclass

from scheme.org.eidr.schema.simple_info_type import SimpleInfoType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class SimpleMetadata(SimpleInfoType):
    class Meta:
        namespace = "http://www.eidr.org/schema"
