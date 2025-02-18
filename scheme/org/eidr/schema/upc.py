from dataclasses import dataclass

from scheme.org.eidr.schema.alternate_idtype import AlternateIdtype

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class Upc(AlternateIdtype):
    """
    UPC is twelve decimal digits.
    """

    class Meta:
        name = "UPC"
