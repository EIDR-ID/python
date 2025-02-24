from dataclasses import dataclass

from    .expression_service_query_type import (
    ExpressionServiceQueryType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class FindServices(ExpressionServiceQueryType):
    class Meta:
        namespace = "http://www.eidr.org/schema"
