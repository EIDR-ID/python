from dataclasses import dataclass

from scheme.org.eidr.schema.service_query_results_type import (
    ServiceQueryResultsType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class ServiceQueryResults(ServiceQueryResultsType):
    class Meta:
        namespace = "http://www.eidr.org/schema"
