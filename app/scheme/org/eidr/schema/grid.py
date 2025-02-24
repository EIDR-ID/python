from dataclasses import dataclass

from    .alternate_idtype import AlternateIdtype

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class Grid(AlternateIdtype):
    """GRid is 2 char (identifier scheme), 5 char (issuer code), 10 char (release
    number), 1 char (check character) Letters must be upper case.

    Either all dashes are present, or none are
    """

    class Meta:
        name = "GRid"
