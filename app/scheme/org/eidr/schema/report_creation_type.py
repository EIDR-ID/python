from enum import Enum

__NAMESPACE__ = "http://www.eidr.org/schema"


class ReportCreationType(Enum):
    BASIC_MOVIE = "BasicMovie"
    BASIC_OTHER = "BasicOther"
    SEASON = "Season"
    INTERACTIVE = "Interactive"
    SERIES = "Series"
    ENCODING = "Encoding"
    EDIT = "Edit"
    CLIP = "Clip"
    COMPOSITE = "Composite"
    COMPILATION = "Compilation"
    EPISODE = "Episode"
    MANIFESTATION = "Manifestation"
