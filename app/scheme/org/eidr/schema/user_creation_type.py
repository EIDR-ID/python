from dataclasses import dataclass, field
from typing import Optional

from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.contact_info_type import (
    ContactInfoType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class UserCreationType:
    """
    Used when creating a user, which is the only time the password is handed
    around.
    """

    class Meta:
        name = "userCreationType"

    parent_party: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParentParty",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
            "pattern": r"10\.5237/[0-9a-fA-F]{4}-[0-9a-fA-F]{4}|10\.5237/superparty",
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
    username: Optional[str] = field(
        default=None,
        metadata={
            "name": "Username",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
            "pattern": r"[0-9a-zA-Z_#\.\-\(\)]{3,32}",
        },
    )
    password: Optional[str] = field(
        default=None,
        metadata={
            "name": "Password",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
            "min_length": 6,
            "max_length": 32,
        },
    )
