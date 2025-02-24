from enum import Enum

__NAMESPACE__ = "http://www.eidr.org/schema"


class SeasonClassType(Enum):
    ADJUNCT = "Adjunct"
    ENHANCED = "Enhanced"
    LIMITED_SERIES = "LimitedSeries"
    MAIN = "Main"
    MINI_SERIES = "Mini-series"
    PRO_FORMA = "Pro Forma"
    RECUT = "Recut"
