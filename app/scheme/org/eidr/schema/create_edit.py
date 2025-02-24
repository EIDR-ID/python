from dataclasses import dataclass

from    .create_edit_data_type import CreateEditDataType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class CreateEdit(CreateEditDataType):
    class Meta:
        namespace = "http://www.eidr.org/schema"
