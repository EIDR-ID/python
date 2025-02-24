from dataclasses import dataclass, field
from typing import Optional

from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.contact_info_type import (
    ContactInfoType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.org_name_type import (
    OrgNameType,
)
from    .administrator_type_type import (
    AdministratorTypeType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class PartyResolutionType:
    """Returned when resolving a party; Used when modifying a party.

    Passwords are modified with a separate call, and not returned when
    resolving.
    """

    class Meta:
        name = "partyResolutionType"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
            "pattern": r"10\.5237/[0-9a-fA-F]{4}-[0-9a-fA-F]{4}|10\.5237/superparty",
        },
    )
    party_name: Optional[OrgNameType] = field(
        default=None,
        metadata={
            "name": "PartyName",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    alternate_party_name: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AlternatePartyName",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "max_occurs": 20,
            "max_length": 256,
        },
    )
    contact_info: Optional[ContactInfoType] = field(
        default=None,
        metadata={
            "name": "ContactInfo",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    active: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Active",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    party_account_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartyAccountName",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "pattern": r"[0-9a-zA-Z_# \.\-\(\)]{2,64}",
        },
    )
    allowed_roles: list[AdministratorTypeType] = field(
        default_factory=list,
        metadata={
            "name": "AllowedRoles",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
