from dataclasses import dataclass, field
from typing import Optional

from    .asset_doitype import AssetDoitype
from    .create_clip_data_type import CreateClipDataType
from    .create_compilation_data_type import (
    CreateCompilationDataType,
)
from    .create_edit_data_type import CreateEditDataType
from    .create_episode_data_type import (
    CreateEpisodeDataType,
)
from    .create_interactive_data_type import (
    CreateInteractiveDataType,
)
from    .create_manifestation_data_type import (
    CreateManifestationDataType,
)
from    .create_season_data_type import CreateSeasonDataType
from    .create_series_data_type import CreateSeriesDataType
from    .creation_type import CreationType
from    .modify_basic_data_type import ModifyBasicDataType
from    .modify_composite_data_type import (
    ModifyCompositeDataType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class ModifyType:
    class Meta:
        name = "modifyType"

    id: Optional[AssetDoitype] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    basic: Optional[ModifyBasicDataType] = field(
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
    composite: Optional[ModifyCompositeDataType] = field(
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
