from enum import Enum

__NAMESPACE__ = "http://www.eidr.org/schema"


class ActiveFilterType(Enum):
    """
    The string is used as a filter to specify the status of a registrant.
    """

    ACTIVE = "active"
    INACTIVE = "inactive"
    ALL = "all"
