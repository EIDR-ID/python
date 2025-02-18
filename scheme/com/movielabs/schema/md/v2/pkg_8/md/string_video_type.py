from enum import Enum

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


class StringVideoType(Enum):
    ANGLE = "angle"
    ENHANCEMENT = "enhancement"
    OVERLAY = "overlay"
    PRIMARY = "primary"
    OTHER = "other"
