from dataclasses import dataclass

from    .create_season_data_type import CreateSeasonDataType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class CreateSeason(CreateSeasonDataType):
    class Meta:
        namespace = "http://www.eidr.org/schema"
