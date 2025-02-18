from dataclasses import dataclass

from scheme.org.eidr.schema.alternate_idtype import AlternateIdtype

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class Afi(AlternateIdtype):
    class Meta:
        name = "AFI"
