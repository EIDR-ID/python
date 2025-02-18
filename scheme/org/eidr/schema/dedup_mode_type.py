from enum import Enum

__NAMESPACE__ = "http://www.eidr.org/schema"


class DedupModeType(Enum):
    NORMAL = "normal"
    MANUAL = "manual"
    ACCEPT = "accept"
    REVIEW = "review"
