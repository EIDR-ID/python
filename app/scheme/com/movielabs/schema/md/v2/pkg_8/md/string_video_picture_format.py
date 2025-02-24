from enum import Enum

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


class StringVideoPictureFormat(Enum):
    VALUE_360 = "360"
    FULL = "Full"
    LETTERBOX = "Letterbox"
    PAN_AND_SCAN = "Pan and Scan"
    PILLARBOX = "Pillarbox"
    STRETCH = "Stretch"
    OTHER = "Other"
