from dataclasses import dataclass, field
from typing import Optional

from scheme.org.eidr.schema.composite_class_type import CompositeClassType
from scheme.org.eidr.schema.composite_element_type import CompositeElementType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class CompositeInfoType:
    class Meta:
        name = "compositeInfoType"

    composite_class: Optional[CompositeClassType] = field(
        default=None,
        metadata={
            "name": "CompositeClass",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    element: list[CompositeElementType] = field(
        default_factory=list,
        metadata={
            "name": "Element",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
