from dataclasses import dataclass

from scheme.org.eidr.schema.service_query_type import ServiceQueryType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class FindServicesFromCatalog(ServiceQueryType):
    class Meta:
        namespace = "http://www.eidr.org/schema"
