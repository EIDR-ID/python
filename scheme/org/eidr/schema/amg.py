from dataclasses import dataclass

from scheme.org.eidr.schema.alternate_idtype import AlternateIdtype

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class Amg(AlternateIdtype):
    """AMG IDs from the V (video) or E (DVD) spaces.

    Can be the letter
    followed by up to 9 digits Future: may want to support othe letter followed by 1-9
    digits left-padded to force field size to be 10
    """

    class Meta:
        name = "AMG"
