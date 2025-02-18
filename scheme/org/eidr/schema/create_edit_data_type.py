from dataclasses import dataclass, field
from typing import Optional

from scheme.org.eidr.schema.creation_self_defined_info import (
    CreationSelfDefinedInfo,
)
from scheme.org.eidr.schema.edit_info_type import EditInfoType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class CreateEditDataType:
    class Meta:
        name = "createEditDataType"

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
        "CreateEditDataType.ExtraObjectMetadata"
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
        edit_info: Optional[EditInfoType] = field(
            default=None,
            metadata={
                "name": "EditInfo",
                "type": "Element",
                "namespace": "http://www.eidr.org/schema",
                "required": True,
            },
        )
