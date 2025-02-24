from enum import Enum

__NAMESPACE__ = "http://www.eidr.org/schema"


class AlternateIdrelationType(Enum):
    CONTAINS_ALL_OF = "ContainsAllOf"
    CONTAINS_PART_OF = "ContainsPartOf"
    DEPICTS_EVENT = "DepictsEvent"
    DEPRECATED = "Deprecated"
    DUPLICATE = "Duplicate"
    HAS_CUE_SHEET = "HasCueSheet"
    HAS_SOUND_RECORDING = "HasSoundRecording"
    IS_DERIVED_FROM = "IsDerivedFrom"
    IS_ENTIRELY_CONTAINED_BY = "IsEntirelyContainedBy"
    IS_PARTIALLY_CONTAINED_BY = "IsPartiallyContainedBy"
    IS_SAME_AS = "IsSameAs"
    IS_SOURCE_OF = "IsSourceOf"
    OTHER = "Other"
