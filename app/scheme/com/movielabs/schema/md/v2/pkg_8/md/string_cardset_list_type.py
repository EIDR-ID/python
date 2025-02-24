from enum import Enum

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


class StringCardsetListType(Enum):
    THEATRICAL = "Theatrical"
    BROADCAST = "Broadcast"
    HOSPITALITY = "Hospitality"
    RENTAL = "Rental"
    EST = "EST"
