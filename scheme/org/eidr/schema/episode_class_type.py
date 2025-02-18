from enum import Enum

__NAMESPACE__ = "http://www.eidr.org/schema"


class EpisodeClassType(Enum):
    MAIN = "Main"
    PILOT = "Pilot"
    STANDALONE = "Standalone"
    SPECIAL = "Special"
    OMNIBUS = "Omnibus"
    RECUT = "Recut"
    SEGMENT = "Segment"
