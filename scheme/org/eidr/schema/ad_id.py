from dataclasses import dataclass

from scheme.org.eidr.schema.alternate_idtype import AlternateIdtype

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class AdId(AlternateIdtype):
    """
    4 alpha chars -- company code 7 alphanumeric -- generated code optional 'H' --
    for HD version.
    """

    class Meta:
        name = "Ad-ID"
