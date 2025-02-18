from enum import Enum

__NAMESPACE__ = "http://www.eidr.org/schema"


class PackagingClassType(Enum):
    DVD = "DVD"
    BD = "BD"
    HD = "HD"
    SD = "SD"
    STREAMING = "Streaming"
    STREAMING_WEB = "Streaming (Web)"
    STREAMING_MOBILE = "Streaming (Mobile)"
    DOWNLOAD_WEB = "Download (Web)"
    DOWNLOAD_MOBILE = "Download (Mobile)"
    VOD = "VOD"
    BROADCAST = "Broadcast"
    DIGITAL_CINEMA = "Digital Cinema"
    OTHER = "Other"
