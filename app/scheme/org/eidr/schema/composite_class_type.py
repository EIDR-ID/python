from enum import Enum

__NAMESPACE__ = "http://www.eidr.org/schema"


class CompositeClassType(Enum):
    MASHUP = "Mashup"
    OMNIBUS = "Omnibus"
    EXCERPT = "Excerpt"
    INCLUSION = "Inclusion"
    OTHER = "Other"
