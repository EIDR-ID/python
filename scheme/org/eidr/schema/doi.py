from dataclasses import dataclass

from scheme.org.eidr.schema.alternate_idtype import AlternateIdtype

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class Doi(AlternateIdtype):
    """
    DOI from outside the eidr system.
    """

    class Meta:
        name = "DOI"
