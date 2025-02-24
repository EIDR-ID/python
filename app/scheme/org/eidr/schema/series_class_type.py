from enum import Enum

__NAMESPACE__ = "http://www.eidr.org/schema"


class SeriesClassType(Enum):
    EPISODIC = "Episodic"
    ANTHOLOGY = "Anthology"
    LIMITED_SERIES = "LimitedSeries"
    MINI_SERIES = "Mini-series"
