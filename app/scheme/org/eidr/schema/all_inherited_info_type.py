from dataclasses import dataclass, field
from typing import Optional

from    .inherited_base_object_info_type import (
    InheritedBaseObjectInfoType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class AllInheritedInfoType:
    """This includes fields that are inherited.

    No data in ExtraObjectMetadata is ever inherited. This is the return
    value for a request to resolve a DOI to its inherited values. See
    API overview for languages and titles. Alternate IDs and
    RegistrantExtra are never inherited.
    """

    class Meta:
        name = "allInheritedInfoType"

    base_object_data: Optional[InheritedBaseObjectInfoType] = field(
        default=None,
        metadata={
            "name": "BaseObjectData",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
