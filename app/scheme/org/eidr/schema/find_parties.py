from dataclasses import dataclass

from    .expression_party_query_type import (
    ExpressionPartyQueryType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class FindParties(ExpressionPartyQueryType):
    class Meta:
        namespace = "http://www.eidr.org/schema"
