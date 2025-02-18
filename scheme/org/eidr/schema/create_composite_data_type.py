from dataclasses import dataclass, field
from typing import Optional

from scheme.org.eidr.schema.composite_info_type import CompositeInfoType
from scheme.org.eidr.schema.creation_full_info import CreationFullInfo

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class CreateCompositeDataType:
    class Meta:
        name = "createCompositeDataType"

    base_object_data: Optional[CreationFullInfo] = field(
        default=None,
        metadata={
            "name": "BaseObjectData",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    extra_object_metadata: Optional[
        "CreateCompositeDataType.ExtraObjectMetadata"
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
