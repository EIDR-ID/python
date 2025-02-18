from dataclasses import dataclass, field
from typing import Optional

from scheme.org.doi.pkg_2010.doischema.party_identifier import PartyIdentifier
from scheme.org.doi.pkg_2010.doischema.party_name import PartyName
from scheme.org.doi.pkg_2010.doischema_avs.agent_role import AgentRole

__NAMESPACE__ = "http://www.doi.org/2010/DOISchema"


@dataclass
class PrincipalAgent:
    """A complex element describing a party principally responsible for the
    creation or publication of a referent.

    Either a 'partyName' or a 'partyIdentifier' element must be present.

    :ivar name: A name by which the principalAgent is known.
    :ivar identifier: An identifier of the principalAgent.
    :ivar role: A role played by the principalAgent.
    """

    class Meta:
        name = "principalAgent"

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
    role: Optional[AgentRole] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.doi.org/2010/DOISchema",
        },
    )
