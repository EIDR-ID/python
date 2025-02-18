from enum import Enum

__NAMESPACE__ = "http://www.eidr.org/schema"


class StatusType(Enum):
    VALID = "valid"
    IN_DEVELOPMENT = "in development"
    ALIAS = "alias"
