from enum import Enum

__NAMESPACE__ = "http://www.eidr.org/schema"


class OperationStatusCodeType(Enum):
    """The status codes that correspond to the third class of statuses: state of each of the operation requests bundled together in a batch"""

    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
