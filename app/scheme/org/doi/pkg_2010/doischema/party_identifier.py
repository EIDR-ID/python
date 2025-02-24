from dataclasses import dataclass, field
from typing import Optional

from app.scheme.org.doi.pkg_2010.doischema_avs.party_identifier_type import (
    PartyIdentifierType,
)

__NAMESPACE__ = "http://www.doi.org/2010/DOISchema"


@dataclass
class PartyIdentifier:
    """
    A complex element describing an identifier used to identify a party.

    :ivar value: A text string representing the value of the
        partyIdentifier (for example, '987654321').
    :ivar type_value: The type of the partyIdentifier.
    """

    class Meta:
        name = "partyIdentifier"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.doi.org/2010/DOISchema",
            "required": True,
        },
    )
    type_value: Optional[PartyIdentifierType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.doi.org/2010/DOISchema",
            "required": True,
        },
    )
