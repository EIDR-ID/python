from dataclasses import dataclass

from scheme.org.eidr.schema.create_composite_data_type import (
    CreateCompositeDataType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class CreateComposite(CreateCompositeDataType):
    class Meta:
        namespace = "http://www.eidr.org/schema"
