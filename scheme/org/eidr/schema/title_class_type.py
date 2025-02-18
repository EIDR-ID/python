from enum import Enum

__NAMESPACE__ = "http://www.eidr.org/schema"


class TitleClassType(Enum):
    """XXX update this list....

    release: title as released
    abbreviated: Prince Caspian for The Chronicles of Narnia: Prince Caspian
    working: working title
    acronym: SATC for Sex and the City
    fan-based: what fans call it
    internal: any
    internal or code name
    series numeric: episodes are identified by number, not name or original broadcast date
    series date: episodes are identified by original broadcast date, not name or number
    regional: regional title that may be in the samelanguage as the original broadcast: if a broadcast release has a different name
    broadcast: the title if it was different when broadcast for the first time, e.g. for a movie shown on TV
    AKA: also known as
    FKA: formerly known as
    transliterated: the title rendered in a script other than the original (e.g. various romanization schemes)
    other:
    """

    RELEASE = "release"
    ABBREVIATED = "abbreviated"
    WORKING = "working"
    ACRONYM = "acronym"
    FAN_BASED = "fan-based"
    INTERNAL = "internal"
    SERIES_NUMERIC = "series numeric"
    SERIES_DATE = "series date"
    REGIONAL = "regional"
    BROADCAST = "broadcast"
    AKA = "AKA"
    FKA = "FKA"
    TRANSLITERATED = "transliterated"
    OTHER = "other"
