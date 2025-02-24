from dataclasses import dataclass, field
from typing import Optional

from app.scheme.org.doi.pkg_2010.doischema_avs.party_name_type import PartyNameType

__NAMESPACE__ = "http://www.doi.org/2010/DOISchema"


@dataclass
class PartyName:
    """
    A complex element describing a name by which a party is known.

    :ivar value: A text string representing the value of the partyName
        (for example, 'John Smith', 'ABC Publishing, Inc').
    :ivar type_value: The type of the partyName.
    """

    class Meta:
        name = "partyName"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.doi.org/2010/DOISchema",
            "required": True,
        },
    )
    type_value: Optional[PartyNameType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.doi.org/2010/DOISchema",
            "required": True,
        },
    )
