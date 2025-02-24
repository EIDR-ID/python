from enum import Enum

__NAMESPACE__ = "http://www.eidr.org/schema"


class ComponentsModeType(Enum):
    """These are a superset of an object's possible mode types; they cover
    individual components and combinations of components.

    "Other" covers combinations not otherwise described

    :cvar AUDIO: Of a Creation which is intended to be listened to.
    :cvar VISUAL: Of a Creation which is intended to be looked at.
    :cvar AUDIO_VISUAL:
    :cvar OTHER:
    :cvar INTERACTIVE_MATERIAL:
    :cvar ALL:
    """

    AUDIO = "Audio"
    VISUAL = "Visual"
    AUDIO_VISUAL = "AudioVisual"
    OTHER = "Other"
    INTERACTIVE_MATERIAL = "InteractiveMaterial"
    ALL = "All"
