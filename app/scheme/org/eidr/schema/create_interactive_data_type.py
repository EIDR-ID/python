from dataclasses import dataclass, field
from typing import Optional

from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.digital_asset_interactive_base_data_type import (
    DigitalAssetInteractiveBaseDataType,
)
from    .creation_self_defined_info import (
    CreationSelfDefinedInfo,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class CreateInteractiveDataType:
    class Meta:
        name = "createInteractiveDataType"

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
        "CreateInteractiveDataType.ExtraObjectMetadata"
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
        interactive_material_info: Optional[
            DigitalAssetInteractiveBaseDataType
        ] = field(
            default=None,
            metadata={
                "name": "InteractiveMaterialInfo",
                "type": "Element",
                "namespace": "http://www.eidr.org/schema",
                "required": True,
            },
        )
