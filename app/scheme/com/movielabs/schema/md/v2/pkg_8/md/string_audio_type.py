from enum import Enum

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


class StringAudioType(Enum):
    COMMENTARY = "commentary"
    DIALOGCENTRIC = "dialogcentric"
    NARRATION = "narration"
    PRIMARY = "primary"
    SILENT = "silent"
    SILENT_OMITTED = "silent-omitted"
    OTHER = "other"
