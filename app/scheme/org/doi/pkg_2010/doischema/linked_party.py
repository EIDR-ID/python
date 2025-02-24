from dataclasses import dataclass, field
from typing import Optional

from app.scheme.org.doi.pkg_2010.doischema.party_identifier import PartyIdentifier
from app.scheme.org.doi.pkg_2010.doischema.party_name import PartyName
from app.scheme.org.doi.pkg_2010.doischema_avs.party_to_party_link_role import (
    PartyToPartyLinkRole,
)

__NAMESPACE__ = "http://www.doi.org/2010/DOISchema"


@dataclass
class LinkedParty:
    """A complex element describing another party with which the referentParty is
    associated.

    At least one of the elements 'partyName' or 'partyIdentifier' must
    be present, and at least one of the elements 'referentPartyRole' or
    'linkedPartyRole'.

    :ivar name: A name by which the linkedParty is known.
    :ivar identifier: An identifier of the linkedParty.
    :ivar referent_party_role: A role played by the referentParty in
        relation to the linkedParty (for example, the referentParty is a
        corporateSubsidiary of the linkedParty).
    :ivar linked_party_role: A role played by the linkedParty in
        relation to the referentParty (for example, the linkedParty is a
        corporateSubsidiary of the referentParty).
    """

    class Meta:
        name = "linkedParty"

    name: Optional[PartyName] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.doi.org/2010/DOISchema",
        },
    )
    identifier: Optional[PartyIdentifier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.doi.org/2010/DOISchema",
        },
    )
    referent_party_role: Optional[PartyToPartyLinkRole] = field(
        default=None,
        metadata={
            "name": "referentPartyRole",
            "type": "Element",
            "namespace": "http://www.doi.org/2010/DOISchema",
        },
    )
    linked_party_role: Optional[PartyToPartyLinkRole] = field(
        default=None,
        metadata={
            "name": "linkedPartyRole",
            "type": "Element",
            "namespace": "http://www.doi.org/2010/DOISchema",
        },
    )
