from dataclasses import dataclass

from scheme.org.eidr.schema.service_alias_continuation_type import (
    ServiceAliasContinuationType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class ServiceAliasContinuation(ServiceAliasContinuationType):
    class Meta:
        namespace = "http://www.eidr.org/schema"
