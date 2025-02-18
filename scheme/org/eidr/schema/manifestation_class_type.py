from enum import Enum

__NAMESPACE__ = "http://www.eidr.org/schema"


class ManifestationClassType(Enum):
    ADAPTATION_SET = "Adaptation Set"
    BLU_RAY = "Blu-ray"
    BROADCAST_PACKAGE = "Broadcast Package"
    CMP = "CMP"
    CPL = "CPL"
    DVD = "DVD"
    EST = "EST"
    GAME_MACHINE = "Game Machine"
    HD = "HD"
    IMF = "IMF"
    MASTER = "Master"
    MEZZANINE = "Mezzanine"
    MOBILE = "Mobile"
    PRESENTATION = "Presentation"
    PROXY = "Proxy"
    REPRESENTATION = "Representation"
    SD = "SD"
    SCREENER = "Screener"
    UHD = "UHD"
    VOD = "VOD"
    VERSION_LANGUAGE = "Version Language"
    WEB = "Web"
    OTHER = "Other"
