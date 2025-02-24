from dataclasses import dataclass

from    .create_basic_data_type import CreateBasicDataType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class CreateBasic(CreateBasicDataType):
    class Meta:
        namespace = "http://www.eidr.org/schema"
