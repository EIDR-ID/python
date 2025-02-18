from enum import Enum

__NAMESPACE__ = "http://www.eidr.org/schema"


class BatchStatusCodeType(Enum):
    """The status codes that correspond to the second class of statuses: state of a submitted batch in the registry"""

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
