from enum import Enum

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


class StringVideoPicType3D(Enum):
    VALUE_2_D_PLUS_DEPTH = "2D-plus-depth"
    ANAGLYPH = "anaglyph"
    CHROMATEK = "Chromatek"
    FRAME_PACKED = "frame-packed"
    IMAX = "IMAX"
    INTERFERENCE_FILTER = "interference-filter"
    LINE_INTERLEAVED = "line-interleaved"
    MASTER_IMAGE = "MasterImage"
    MULTISCOPIC = "multiscopic"
    MVC = "MVC"
    OVER_UNDER = "over-under"
    PULFRICH = "Pulfrich"
    QUINCUNX = "quincunx"
    REAL_D = "RealD"
    SENSIO = "Sensio"
    SIDE_BY_SIDE = "side-by-side"
    XPAN_D = "XpanD"
