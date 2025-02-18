from dataclasses import dataclass

from scheme.org.eidr.schema.service_resolution_type import (
    ServiceResolutionType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class Service(ServiceResolutionType):
    class Meta:
        namespace = "http://www.eidr.org/schema"
