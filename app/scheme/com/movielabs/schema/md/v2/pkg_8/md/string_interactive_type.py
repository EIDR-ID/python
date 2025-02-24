from enum import Enum

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


class StringInteractiveType(Enum):
    VALUE_360 = "360"
    AR = "AR"
    COMIC = "Comic"
    COMMERCE = "Commerce"
    IMAGE = "Image"
    INTERACTIVITY = "Interactivity"
    LIVE = "Live"
    LOCATION = "Location"
    MR = "MR"
    MENU = "Menu"
    MIXED_MEDIA = "Mixed-Media"
    OVERLAY_GAME = "Overlay Game"
    SKINS = "Skins"
    STANDALONE_GAME = "Standalone Game"
    VR = "VR"
    OTHER = "Other"
