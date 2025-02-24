from enum import Enum

__NAMESPACE__ = "http://www.eidr.org/schema"


class LanguageTrackTypeType(Enum):
    COMMENTARY = "commentary"
    DIALOGCENTRIC = "dialogcentric"
    NARRATION = "narration"
    PRIMARY = "primary"
    SILENT = "silent"
    SILENT_OMITTED = "silent-omitted"
    OTHER = "other"
    EASYREADER = "easyreader"
    FORCED = "forced"
    LARGE = "large"
    NOFORCED = "noforced"
    NORMAL = "normal"
    SDH = "SDH"
    SINGALONG = "singalong"
