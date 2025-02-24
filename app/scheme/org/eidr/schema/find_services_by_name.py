from dataclasses import dataclass

from    .service_query_type import ServiceQueryType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class FindServicesByName(ServiceQueryType):
    class Meta:
        namespace = "http://www.eidr.org/schema"
