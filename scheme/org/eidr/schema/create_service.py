from dataclasses import dataclass

from scheme.org.eidr.schema.service_creation_type import ServiceCreationType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class CreateService(ServiceCreationType):
    class Meta:
        namespace = "http://www.eidr.org/schema"
