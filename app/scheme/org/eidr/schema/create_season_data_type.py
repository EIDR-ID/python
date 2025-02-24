from dataclasses import dataclass, field
from typing import Optional

from    .creation_self_defined_info import (
    CreationSelfDefinedInfo,
)
from   .season_info_type import SeasonInfoType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class CreateSeasonDataType:
    """
    A Season must be the child of a Series.
    """

    class Meta:
        name = "createSeasonDataType"

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
        "CreateSeasonDataType.ExtraObjectMetadata"
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
        season_info: Optional[SeasonInfoType] = field(
            default=None,
            metadata={
                "name": "SeasonInfo",
                "type": "Element",
                "namespace": "http://www.eidr.org/schema",
                "required": True,
            },
        )
