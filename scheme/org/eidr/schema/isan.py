from dataclasses import dataclass

from scheme.org.eidr.schema.alternate_idtype import AlternateIdtype

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class Isan(AlternateIdtype):
    """ISAN in form 4-4-4-4, 4-4-4-4-C (C is a checkdigit), 4-4-4-4-C-4-4-C, or
    4-4-4-4-4-4 Hex digits and check digits must be upper case All occurrences in a
    string of "-" must be one of dash, space or nothing.

    The 24-digit forms must have both check digits, or neither.
    """

    class Meta:
        name = "ISAN"
