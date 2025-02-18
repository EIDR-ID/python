from enum import Enum

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


class ColorTypeType(Enum):
    COLOR = "color"
    BANDW = "bandw"
    COLORIZED = "colorized"
    COMPOSITE = "composite"
    UNKNOWN = "unknown"
