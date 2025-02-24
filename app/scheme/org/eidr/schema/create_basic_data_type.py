from dataclasses import dataclass, field
from typing import Optional

from    .creation_full_info import CreationFullInfo

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class CreateBasicDataType:
    class Meta:
        name = "createBasicDataType"

    base_object_data: Optional[CreationFullInfo] = field(
        default=None,
        metadata={
            "name": "BaseObjectData",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
