from dataclasses import dataclass, field
from typing import Optional

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
from scheme.org.eidr.schema.creation_type import CreationType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class CreateType:
    class Meta:
        name = "createType"

    basic: Optional[CreateBasicDataType] = field(
        default=None,
        metadata={
            "name": "Basic",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    series: Optional[CreateSeriesDataType] = field(
        default=None,
        metadata={
            "name": "Series",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    interactive: Optional[CreateInteractiveDataType] = field(
        default=None,
        metadata={
            "name": "Interactive",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    season: Optional[CreateSeasonDataType] = field(
        default=None,
        metadata={
            "name": "Season",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    episode: Optional[CreateEpisodeDataType] = field(
        default=None,
        metadata={
            "name": "Episode",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    manifestation: Optional[CreateManifestationDataType] = field(
        default=None,
        metadata={
            "name": "Manifestation",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    edit: Optional[CreateEditDataType] = field(
        default=None,
        metadata={
            "name": "Edit",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    clip: Optional[CreateClipDataType] = field(
        default=None,
        metadata={
            "name": "Clip",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    compilation: Optional[CreateCompilationDataType] = field(
        default=None,
        metadata={
            "name": "Compilation",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    composite: Optional[CreateCompositeDataType] = field(
        default=None,
        metadata={
            "name": "Composite",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    type_value: Optional[CreationType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
