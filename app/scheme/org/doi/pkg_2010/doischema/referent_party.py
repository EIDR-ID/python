from dataclasses import dataclass, field
from typing import Optional

from app.scheme.org.doi.pkg_2010.doischema.date import Date
from app.scheme.org.doi.pkg_2010.doischema.linked_party import LinkedParty
from app.scheme.org.doi.pkg_2010.doischema.party_identifier import PartyIdentifier
from app.scheme.org.doi.pkg_2010.doischema.party_name import PartyName
from app.scheme.org.doi.pkg_2010.doischema_avs.associated_party_role import (
    AssociatedPartyRole,
)
from app.scheme.org.doi.pkg_2010.doischema_avs.party_structural_type import (
    PartyStructuralType,
)
from app.scheme.org.doi.pkg_2010.doischema_avs.territory_code import TerritoryCode

__NAMESPACE__ = "http://www.doi.org/2010/DOISchema"


@dataclass
class ReferentParty:
    """
    A complex element describing the party identified by the doiName to which the
    kernelMetadata applies.

    :ivar name: A name by which the referentParty is known. For Kernel
        Metadata in a restricted Application Profile the string 'No
        information available' should be used, with a partyNameType of
        'name'.
    :ivar identifier: An identifier of the referentParty.
    :ivar structural_type: The primary structuralType of the
        referentParty.
    :ivar associated_role: For parties, the referentType represents a
        role with which the party is commonly associated, not
        necessarily a permanent type.
    :ivar date_of_birth_or_formation: The date of birth (for an
        individual or animal) or formation (for an organization) of the
        referentParty. If an organization was (re)formed on one or more
        occasion, this date should represent the latest date of
        formation.
    :ivar date_of_death_or_dissolution: The date of death (for an
        individual or animal) or dissolution (for an organization) of
        the referentParty. If an organization was dissolved on one or
        more occasion, this date should represent the latest date of
        dissolution.
    :ivar associated_territory: A territory with which the referentParty
        is associated (for example, a territory of birth, nationality or
        residence). As with other elements (dates and referentType) this
        element is included to support the disambiguation of one party
        with another.
    :ivar linked_party: Another party to whom the referentParty is
        linked, with identification of link role (eg member, department,
        corporate subsiduary, child, sibling). This element is included
        in Kernel Metadata as it may be critical for the identification
        of an organization which exists only as part of another
        organization.
    """

    class Meta:
        name = "referentParty"

    name: list[PartyName] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.doi.org/2010/DOISchema",
            "min_occurs": 1,
        },
    )
    identifier: list[PartyIdentifier] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.doi.org/2010/DOISchema",
        },
    )
    structural_type: Optional[PartyStructuralType] = field(
        default=None,
        metadata={
            "name": "structuralType",
            "type": "Element",
            "namespace": "http://www.doi.org/2010/DOISchema",
            "required": True,
        },
    )
    associated_role: list[AssociatedPartyRole] = field(
        default_factory=list,
        metadata={
            "name": "associatedRole",
            "type": "Element",
            "namespace": "http://www.doi.org/2010/DOISchema",
            "min_occurs": 1,
        },
    )
    date_of_birth_or_formation: Optional[Date] = field(
        default=None,
        metadata={
            "name": "dateOfBirthOrFormation",
            "type": "Element",
            "namespace": "http://www.doi.org/2010/DOISchema",
        },
    )
    date_of_death_or_dissolution: Optional[Date] = field(
        default=None,
        metadata={
            "name": "dateOfDeathOrDissolution",
            "type": "Element",
            "namespace": "http://www.doi.org/2010/DOISchema",
        },
    )
    associated_territory: list[TerritoryCode] = field(
        default_factory=list,
        metadata={
            "name": "associatedTerritory",
            "type": "Element",
            "namespace": "http://www.doi.org/2010/DOISchema",
        },
    )
    linked_party: list[LinkedParty] = field(
        default_factory=list,
        metadata={
            "name": "linkedParty",
            "type": "Element",
            "namespace": "http://www.doi.org/2010/DOISchema",
        },
    )
