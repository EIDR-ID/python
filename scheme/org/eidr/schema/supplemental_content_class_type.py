from enum import Enum

__NAMESPACE__ = "http://www.eidr.org/schema"


class SupplementalContentClassType(Enum):
    B_ROLL = "B-roll"
    BEHIND_THE_SCENES = "Behind the scenes"
    DELETED_SCENE = "Deleted Scene"
    FEATURETTE = "Featurette"
    INTERACTIVITY = "Interactivity"
    INTERVIEW = "Interview"
    MAKING_OF = "Making Of"
    MUSIC_VIDEO = "Music Video"
    MUSIC = "Music"
    OUTTAKE = "Outtake"
    SCREEN_TEST = "Screen Test"
    SELECTED_CLIPS = "Selected Clips"
    OTHER = "Other"
