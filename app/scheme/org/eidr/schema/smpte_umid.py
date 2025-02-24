from dataclasses import dataclass

from    .alternate_idtype import AlternateIdtype

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class SmpteUmid(AlternateIdtype):
    class Meta:
        name = "SMPTE-UMID"
