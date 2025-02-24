from enum import Enum

__NAMESPACE__ = "http://www.eidr.org/schema"


class AlternateContentClassType(Enum):
    ALTERNATE_SCENE = "Alternate Scene"
    CAMERA_ANGLE = "Camera Angle"
    CENSORED = "Censored"
    COMMENTARY_DIRECTOR = "Commentary (Director)"
    COMMENTARY_OTHER = "Commentary (Other)"
    DESCRIPTIVE_AUDIO = "Descriptive Audio"
    PARENTAL_CONTROL = "Parental Control"
    SING_ALONG = "Sing Along"
    TRIVIA_TRACK = "Trivia Track"
    OTHER = "Other"
