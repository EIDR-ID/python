from dataclasses import dataclass, field
from typing import Optional

from    .episode_info_type import EpisodeInfoType
from   .season_info_type import SeasonInfoType
from    .series_info_type import SeriesInfoType
from    .simple_info_type import SimpleInfoType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class SeriesAncestryType:
    class Meta:
        name = "seriesAncestryType"

    origin: Optional[SimpleInfoType] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    episode_basic_data: Optional[SimpleInfoType] = field(
        default=None,
        metadata={
            "name": "EpisodeBasicData",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    episode_info: Optional[EpisodeInfoType] = field(
        default=None,
        metadata={
            "name": "EpisodeInfo",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    season_basic_data: Optional[SimpleInfoType] = field(
        default=None,
        metadata={
            "name": "SeasonBasicData",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    season_info: Optional[SeasonInfoType] = field(
        default=None,
        metadata={
            "name": "SeasonInfo",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    series_basic_data: Optional[SimpleInfoType] = field(
        default=None,
        metadata={
            "name": "SeriesBasicData",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    series_info: Optional[SeriesInfoType] = field(
        default=None,
        metadata={
            "name": "SeriesInfo",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
