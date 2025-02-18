from dataclasses import dataclass

from scheme.org.eidr.schema.create_series_data_type import CreateSeriesDataType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class CreateSeries(CreateSeriesDataType):
    class Meta:
        namespace = "http://www.eidr.org/schema"
