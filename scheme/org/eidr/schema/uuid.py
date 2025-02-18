from dataclasses import dataclass

from scheme.org.eidr.schema.alternate_idtype import AlternateIdtype

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class Uuid(AlternateIdtype):
    """UUID in form 8-4-4-4-12.

    Both upper and lowercase hex digits allowed.
    """

    class Meta:
        name = "UUID"
