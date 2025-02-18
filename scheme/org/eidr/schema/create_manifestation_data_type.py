from dataclasses import dataclass, field
from typing import Optional

from scheme.org.eidr.schema.creation_self_defined_info import (
    CreationSelfDefinedInfo,
)
from scheme.org.eidr.schema.manifestation_info_type import (
    ManifestationInfoType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class CreateManifestationDataType:
    class Meta:
        name = "createManifestationDataType"

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
        "CreateManifestationDataType.ExtraObjectMetadata"
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
        manifestation_info: Optional[ManifestationInfoType] = field(
            default=None,
            metadata={
                "name": "ManifestationInfo",
                "type": "Element",
                "namespace": "http://www.eidr.org/schema",
                "required": True,
            },
        )
