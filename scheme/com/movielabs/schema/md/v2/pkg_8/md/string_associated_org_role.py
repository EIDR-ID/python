from enum import Enum

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


class StringAssociatedOrgRole(Enum):
    PRODUCER = "producer"
    DISTRIBUTOR = "distributor"
    BROADCASTER = "broadcaster"
    EDITOR = "editor"
    ENCODER = "encoder"
    OTHER = "other"
