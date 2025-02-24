from dataclasses import dataclass

from    .alternate_idtype import AlternateIdtype

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class Imdb(AlternateIdtype):
    class Meta:
        name = "IMDB"
