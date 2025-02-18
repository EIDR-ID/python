from dataclasses import dataclass, field
from typing import Optional

from scheme.org.eidr.schema.base_object_info_type import BaseObjectInfoType
from scheme.org.eidr.schema.extra_object_metadata_type import (
    ExtraObjectMetadataType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class FullObjectInfoType:
    """This contains all the information about the object.

    This is the return value for a request for full resolution of an
    asset DOI. In baseObjectData all mandatory fields are provided
    (either by inheritance or actual presence.) The languages fields are
    fuly realized, based on the inheritance, add, and replace chain from
    all ancestors. ExtraObjectmetadata contains metadata for any
    described type information or relationships or relationships that
    are present. (See extraObjectMetadataType for the legal
    combinations.)
    """

    class Meta:
        name = "fullObjectInfoType"

    base_object_data: Optional[BaseObjectInfoType] = field(
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
