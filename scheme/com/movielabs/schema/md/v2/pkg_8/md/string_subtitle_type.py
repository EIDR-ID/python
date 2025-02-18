from enum import Enum

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


class StringSubtitleType(Enum):
    COMMENTARY = "commentary"
    EASYREADER = "easyreader"
    FORCED = "forced"
    LARGE = "large"
    NOFORCED = "noforced"
    NORMAL = "normal"
    SDH = "SDH"
    SINGALONG = "singalong"
    OTHER = "other"
