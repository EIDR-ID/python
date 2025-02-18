from dataclasses import dataclass

from scheme.org.eidr.schema.create_episode_data_type import (
    CreateEpisodeDataType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class CreateEpisode(CreateEpisodeDataType):
    class Meta:
        namespace = "http://www.eidr.org/schema"
