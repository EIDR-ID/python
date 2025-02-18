from dataclasses import dataclass, field
from typing import Optional

from scheme.org.eidr.schema.extra_object_metadata_type import (
    ExtraObjectMetadataType,
)
from scheme.org.eidr.schema.self_defined_base_object_info_type import (
    SelfDefinedBaseObjectInfoType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class AllSelfDefinedInfoType:
    """Contains all the fields defined on the object itself.

    This is the return value for a request for resolution of a DOI to
    its 'own' information.
    """

    class Meta:
        name = "allSelfDefinedInfoType"

    base_object_data: Optional[SelfDefinedBaseObjectInfoType] = field(
        default=None,
        metadata={
            "name": "BaseObjectData",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    extra_object_metadata: Optional[ExtraObjectMetadataType] = field(
        default=None,
        metadata={
            "name": "ExtraObjectMetadata",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
