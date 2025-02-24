from dataclasses import dataclass, field
from typing import Optional

from    .clip_info_type import ClipInfoType
from    .creation_self_defined_info import (
    CreationSelfDefinedInfo,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class CreateClipDataType:
    class Meta:
        name = "createClipDataType"

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
        "CreateClipDataType.ExtraObjectMetadata"
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
        clip_info: Optional[ClipInfoType] = field(
            default=None,
            metadata={
                "name": "ClipInfo",
                "type": "Element",
                "namespace": "http://www.eidr.org/schema",
                "required": True,
            },
        )
