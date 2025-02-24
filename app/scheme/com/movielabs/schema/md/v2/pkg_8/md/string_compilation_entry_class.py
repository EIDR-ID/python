from enum import Enum

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


class StringCompilationEntryClass(Enum):
    EPISODE = "Episode"
    INSTALLMENT = "Installment"
    PART = "Part"
    SEASON = "Season"
    SUPPLEMENTAL = "Supplemental"
