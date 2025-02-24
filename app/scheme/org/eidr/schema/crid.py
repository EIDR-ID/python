from dataclasses import dataclass

from    .alternate_idtype import AlternateIdtype

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class Crid(AlternateIdtype):
    """A CRID is crid://dns name/data (see rfc 4078) 'crid' is case-insensitive
    this regular expression for the domain requires at least one .

    in the domain, and supports 2-4 character top level domains the
    other pieces of the domain are alphanumeric first char, alphanumeric
    or dash in the middle, alphanumeric last char, maximum 63 characters
    data: doesn't include ? or # sections yet, and may be too
    restrictive
    """

    class Meta:
        name = "CRID"
