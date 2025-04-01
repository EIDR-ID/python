from enum import Enum
from typing import Union


def get_enum(enum_class, enum_value: Union[Enum, str]):
    """
    Get the corresponding enum value and is flexible to centralize a function for consistency.
    :param enum_class: the class of the enum
    :param enum_value: the value of the enum being either a string or an enum
    """
    ret = None
    if isinstance(enum_value, str):
        enum_values = [enum.value for enum in enum_class]
        if enum_value not in enum_values:
            raise ValueError(f"'{enum_value}' is an invalid enum, must be one of the following: {enum_values}")
        ret = enum_class(enum_value)
    elif isinstance(enum_value, Enum):
        ret = enum_value
    return ret
