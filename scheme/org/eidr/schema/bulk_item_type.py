from dataclasses import dataclass, field
from typing import Optional

from scheme.org.eidr.schema.composite_info_type import CompositeInfoType
from scheme.org.eidr.schema.create_basic_data_type import CreateBasicDataType
from scheme.org.eidr.schema.create_clip_data_type import CreateClipDataType
from scheme.org.eidr.schema.create_compilation_data_type import (
    CreateCompilationDataType,
)
from scheme.org.eidr.schema.create_composite_data_type import (
    CreateCompositeDataType,
)
from scheme.org.eidr.schema.create_edit_data_type import CreateEditDataType
from scheme.org.eidr.schema.create_episode_data_type import (
    CreateEpisodeDataType,
)
from scheme.org.eidr.schema.create_interactive_data_type import (
    CreateInteractiveDataType,
)
from scheme.org.eidr.schema.create_manifestation_data_type import (
    CreateManifestationDataType,
)
from scheme.org.eidr.schema.create_season_data_type import CreateSeasonDataType
from scheme.org.eidr.schema.create_series_data_type import CreateSeriesDataType
from scheme.org.eidr.schema.dedup_mode_type import DedupModeType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class BulkItemType:
    class Meta:
        name = "bulkItemType"

    local_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocalID",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
            "pattern": r"LOCAL:[0-9a-zA-Z_#/\.\-\(\)]{1,128}",
        },
    )
    create_basic: Optional[CreateBasicDataType] = field(
        default=None,
        metadata={
            "name": "CreateBasic",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    create_season: Optional[CreateSeasonDataType] = field(
        default=None,
        metadata={
            "name": "CreateSeason",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    create_interactive: Optional[CreateInteractiveDataType] = field(
        default=None,
        metadata={
            "name": "CreateInteractive",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    create_series: Optional[CreateSeriesDataType] = field(
        default=None,
        metadata={
            "name": "CreateSeries",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    create_manifestation: Optional[CreateManifestationDataType] = field(
        default=None,
        metadata={
            "name": "CreateManifestation",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    create_edit: Optional[CreateEditDataType] = field(
        default=None,
        metadata={
            "name": "CreateEdit",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    create_clip: Optional[CreateClipDataType] = field(
        default=None,
        metadata={
            "name": "CreateClip",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    create_composite: Optional[CreateCompositeDataType] = field(
        default=None,
        metadata={
            "name": "CreateComposite",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    create_episode: Optional[CreateEpisodeDataType] = field(
        default=None,
        metadata={
            "name": "CreateEpisode",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    create_compilation: Optional[CreateCompilationDataType] = field(
        default=None,
        metadata={
            "name": "CreateCompilation",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    composite_info: Optional[CompositeInfoType] = field(
        default=None,
        metadata={
            "name": "CompositeInfo",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    dedup_mode: Optional[DedupModeType] = field(
        default=None,
        metadata={
            "name": "dedupMode",
            "type": "Attribute",
        },
    )
