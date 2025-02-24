from enum import Enum

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


class StringSubtitleFormatType(Enum):
    VALUE_3_GPP = "3GPP"
    BLU_RAY = "Blu-ray"
    CAP = "CAP"
    CFF_TT = "CFF-TT"
    DCI = "DCI"
    DVB = "DVB"
    DVD = "DVD"
    DXFP = "DXFP"
    IMSC1 = "IMSC1"
    ITT = "ITT"
    SCC = "SCC"
    SMPTE_2052_1_TIMED_TEXT = "SMPTE 2052-1 Timed Text"
    SRT = "SRT"
    STL = "STL"
    TTML = "TTML"
    WEB_VTT = "WebVTT"
