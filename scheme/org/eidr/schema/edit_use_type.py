from enum import Enum

__NAMESPACE__ = "http://www.eidr.org/schema"


class EditUseType(Enum):
    """These are intended to capture the original, primary, intended use for the
    Edit.

    In many cases, the actual uses will be different, e.g., iTunes using
    the Theatrical cut.
    """

    AIRLINE = "Airline"
    BROADCAST = "Broadcast"
    HOME_VIDEO = "Home Video"
    HOSPITALITY = "Hospitality"
    MULTIUSE = "Multiuse"
    PRESERVATION_MASTER = "Preservation Master"
    STREAMING = "Streaming"
    THEATRICAL = "Theatrical"
    WEB = "Web"
    UNKNOWN = "Unknown"
