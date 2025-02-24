from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class ContactInfoType:
    class Meta:
        name = "ContactInfo-type"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
    primary_email: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrimaryEmail",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
    alternate_email: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AlternateEmail",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    address: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    phone: list["ContactInfoType.Phone"] = field(
        default_factory=list,
        metadata={
            "name": "Phone",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )

    @dataclass
    class Phone:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        type_value: Optional[str] = field(
            default=None,
            metadata={
                "name": "type",
                "type": "Attribute",
            },
        )
