from enum import Enum

__NAMESPACE__ = "http://www.eidr.org/schema"


class OperationStatusTypeType(Enum):
    """The status types that correspond to the third class of statuses: state of each of the operation requests bundled together in a batch"""

    SUCCESS = "success"
    DUPLICATE = "duplicate"
    PENDING = "pending"
    AUTHORIZATION_ERROR = "authorization error"
    VALIDATION_ERROR = "validation error"
    OTHER_ERROR = "other error"
    REJECTED = "rejected"
