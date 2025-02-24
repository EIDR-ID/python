from dataclasses import dataclass

from    .alternate_idtype import AlternateIdtype

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class Muze(AlternateIdtype):
    class Meta:
        name = "MUZE"
