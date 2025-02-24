from dataclasses import dataclass

from    .report_query_type import ReportQueryType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class DetailReport(ReportQueryType):
    class Meta:
        namespace = "http://www.eidr.org/schema"
