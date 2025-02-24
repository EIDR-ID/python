from dataclasses import dataclass, field
from typing import Optional

from    .creation_self_defined_info import (
    CreationSelfDefinedInfo,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class ModifyBasicDataType:
    class Meta:
        name = "modifyBasicDataType"

    base_object_data: Optional[CreationSelfDefinedInfo] = field(
        default=None,
        metadata={
            "name": "BaseObjectData",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
