from dataclasses import dataclass, field
from typing import Optional

from    .creation_self_defined_info import (
    CreationSelfDefinedInfo,
)
from    .episode_info_type import EpisodeInfoType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class CreateEpisodeDataType:
    """
    An Episode must be the child of a Series or a Season.
    """

    class Meta:
        name = "createEpisodeDataType"

    base_object_data: Optional[CreationSelfDefinedInfo] = field(
        default=None,
        metadata={
            "name": "BaseObjectData",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    extra_object_metadata: Optional[
        "CreateEpisodeDataType.ExtraObjectMetadata"
    ] = field(
        default=None,
        metadata={
            "name": "ExtraObjectMetadata",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )

    @dataclass
    class ExtraObjectMetadata:
        episode_info: Optional[EpisodeInfoType] = field(
            default=None,
            metadata={
                "name": "EpisodeInfo",
                "type": "Element",
                "namespace": "http://www.eidr.org/schema",
                "required": True,
            },
        )
