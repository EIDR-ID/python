from dataclasses import dataclass, field
from typing import Optional

from    .composite_info_type import CompositeInfoType
from    .creation_self_defined_info import (
    CreationSelfDefinedInfo,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class ModifyCompositeDataType:
    class Meta:
        name = "modifyCompositeDataType"

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
        "ModifyCompositeDataType.ExtraObjectMetadata"
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
        composite_info: Optional[CompositeInfoType] = field(
            default=None,
            metadata={
                "name": "CompositeInfo",
                "type": "Element",
                "namespace": "http://www.eidr.org/schema",
                "required": True,
            },
        )
