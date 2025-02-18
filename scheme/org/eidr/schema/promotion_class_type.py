from enum import Enum

__NAMESPACE__ = "http://www.eidr.org/schema"


class PromotionClassType(Enum):
    BROADCAST_AD = "Broadcast Ad"
    DVD_TRAILER = "DVD Trailer"
    EPK = "EPK"
    INFOMERCIAL = "Infomercial"
    MOBILE = "Mobile"
    PREVIEW = "Preview"
    RADIO_SPOT = "Radio Spot"
    SIZZLE_REEL = "Sizzle Reel"
    TEASER = "Teaser"
    THEATRICAL_TRAILER = "Theatrical Trailer"
    UGC_SITE = "UGC Site"
    WEB = "Web"
    OTHER = "Other"
