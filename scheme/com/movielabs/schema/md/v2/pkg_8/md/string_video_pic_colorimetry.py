from enum import Enum

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


class StringVideoPicColorimetry(Enum):
    VALUE_601 = "601"
    VALUE_709 = "709"
    VALUE_2020 = "2020"
    P3 = "P3"
    XV_YCC709 = "xvYCC709"
