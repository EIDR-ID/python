from dataclasses import dataclass

from    .alternate_idtype import AlternateIdtype

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class Istc(AlternateIdtype):
    """3 hex digits, 4 digits, 8 hex digits, ISO 7064 MOD16-3 check digit (The
    groups can be separated by nothing, a space, or a hyphen.

    The same separator must be used for the whole ID.)
    """

    class Meta:
        name = "ISTC"
