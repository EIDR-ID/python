from enum import Enum

__NAMESPACE__ = "http://www.doi.org/2010/DOISchemaAVS"


class Mode(Enum):
    """Allowed values for sensory modes with which a Creation is intended to be
    perceived.

    If the creation is an abstraction, this value may be used to refer
    to the mode in which manifestations of the abstraction can be
    expressed. For example, a musical work is abstraction that may be
    expressed in a performance (audio), in notational form (visual) or
    in braille notation (tangible).

    :cvar AUDIO: Of a Creation which is intended to be listened to.
    :cvar OLFACTORY: Of a Creation which is intended to be smelled.
    :cvar RESTRICTED: A Creation identified within a restricted DOI
        Application Profile for which kernel metadata values are not
        generally available.
    :cvar TANGIBLE: Of a Creation which is intended to be touched.
    :cvar TASTEABLE: Of a Creation which is intended to be tasted.
    :cvar VISUAL: Of a Creation which is intended to be looked at.
    """

    AUDIO = "Audio"
    OLFACTORY = "Olfactory"
    RESTRICTED = "Restricted"
    TANGIBLE = "Tangible"
    TASTEABLE = "Tasteable"
    VISUAL = "Visual"
