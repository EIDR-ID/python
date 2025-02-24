from enum import Enum

__NAMESPACE__ = "http://www.eidr.org/schema"


class CreationType(Enum):
    CREATE_BASIC = "CreateBasic"
    CREATE_SEASON = "CreateSeason"
    CREATE_INTERACTIVE = "CreateInteractive"
    CREATE_SERIES = "CreateSeries"
    CREATE_MANIFESTATION = "CreateManifestation"
    CREATE_EDIT = "CreateEdit"
    CREATE_CLIP = "CreateClip"
    CREATE_COMPOSITE = "CreateComposite"
    CREATE_COMPILATION = "CreateCompilation"
    CREATE_EPISODE = "CreateEpisode"
