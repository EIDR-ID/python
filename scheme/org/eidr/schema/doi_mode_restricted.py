from enum import Enum

__NAMESPACE__ = "http://www.eidr.org/schema"


class DoiModeRestricted(Enum):
    """
    :cvar AUDIO: Of a Creation which is intended to be listened to.
    :cvar VISUAL: Of a Creation which is intended to be looked at.
    """

    AUDIO = "Audio"
    VISUAL = "Visual"
