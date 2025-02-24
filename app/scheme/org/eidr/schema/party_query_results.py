from dataclasses import dataclass

from    .party_query_results_type import (
    PartyQueryResultsType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class PartyQueryResults(PartyQueryResultsType):
    class Meta:
        namespace = "http://www.eidr.org/schema"
