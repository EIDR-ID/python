from dataclasses import dataclass

from scheme.org.eidr.schema.create_compilation_data_type import (
    CreateCompilationDataType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class CreateCompilation(CreateCompilationDataType):
    class Meta:
        namespace = "http://www.eidr.org/schema"
