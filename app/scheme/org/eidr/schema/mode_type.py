from enum import Enum

__NAMESPACE__ = "http://www.eidr.org/schema"


class ModeType(Enum):
    """
    Use DOI types where possible; use Other for InteractiveMaterial; AudioVisual is
    included for compatibility with DOI 2004 modes.

    :cvar AUDIO: Of a Creation which is intended to be listened to.
    :cvar VISUAL: Of a Creation which is intended to be looked at.
    :cvar AUDIO_VISUAL:
    :cvar OTHER:
    """

    AUDIO = "Audio"
    VISUAL = "Visual"
    AUDIO_VISUAL = "AudioVisual"
    OTHER = "Other"
