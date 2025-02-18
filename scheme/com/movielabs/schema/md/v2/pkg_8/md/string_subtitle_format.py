from enum import Enum

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


class StringSubtitleFormat(Enum):
    TEXT = "Text"
    IMAGE = "Image"
    COMBINED = "Combined"
