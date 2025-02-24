from enum import Enum

__NAMESPACE__ = "http://www.doi.org/2010/DOISchemaAVS"


class TimeProximity(Enum):
    """Allowed values for the proximity of a declared time to the actual time
    referenced.

    A null value indicates that the date is accurate.

    :cvar AFTER: A time which is after the time stated.
    :cvar BEFORE: A time which is before the time stated.
    :cvar CIRCA: A time which is approximately accurate.
    :cvar NOT_AFTER: A time which is the same as or before the time
        stated.
    :cvar NOT_BEFORE: A time which is the same as or after the time
        stated.
    """

    AFTER = "After"
    BEFORE = "Before"
    CIRCA = "Circa"
    NOT_AFTER = "NotAfter"
    NOT_BEFORE = "NotBefore"
