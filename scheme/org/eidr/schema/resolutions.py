from dataclasses import dataclass

from scheme.org.eidr.schema.resolution_set_type import ResolutionSetType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class Resolutions(ResolutionSetType):
    class Meta:
        namespace = "http://www.eidr.org/schema"
