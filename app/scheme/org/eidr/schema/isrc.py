from dataclasses import dataclass

from    .alternate_idtype import AlternateIdtype

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class Isrc(AlternateIdtype):
    """An ISRC is 2-char (non-digit) country code, 3 char (alpha or digit)
    registrant code, 2 digit year of reference, 5 digit designation code, with
    optional separating dashes.

    Letters are upper case. Either all dashes are present, or none are.
    """

    class Meta:
        name = "ISRC"
