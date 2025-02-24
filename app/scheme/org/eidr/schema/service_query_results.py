from dataclasses import dataclass

from    .service_query_results_type import (
    ServiceQueryResultsType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class ServiceQueryResults(ServiceQueryResultsType):
    class Meta:
        namespace = "http://www.eidr.org/schema"
