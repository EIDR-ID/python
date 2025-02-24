from enum import Enum

__NAMESPACE__ = "http://www.eidr.org/schema"


class BatchStatusTypeType(Enum):
    """The status types that correspond to the second class of statuses: state of a submitted batch in the registry"""

    BATCH_RECEIVED = "batch received"
    BATCH_QUEUED = "batch queued"
    INVALID_BATCH = "invalid batch"
