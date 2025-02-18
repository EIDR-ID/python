from dataclasses import dataclass, field
from typing import Optional

from scheme.com.movielabs.schema.md.v2.pkg_8.md.associated_org_type import (
    AssociatedOrgType,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class ComplianceType:
    class Meta:
        name = "Compliance-type"

    category: Optional[str] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    standard: Optional[str] = field(
        default=None,
        metadata={
            "name": "Standard",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    disposition: Optional[str] = field(
        default=None,
        metadata={
            "name": "Disposition",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
    competent_authority: Optional[AssociatedOrgType] = field(
        default=None,
        metadata={
            "name": "CompetentAuthority",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    certificate: Optional["ComplianceType.Certificate"] = field(
        default=None,
        metadata={
            "name": "Certificate",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    testing_organization: Optional[AssociatedOrgType] = field(
        default=None,
        metadata={
            "name": "TestingOrganization",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    testing_method: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestingMethod",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    comments: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comments",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )

    @dataclass
    class Certificate:
        value: Optional[bytes] = field(
            default=None,
            metadata={
                "required": True,
                "format": "base64",
            },
        )
        mime: Optional[str] = field(
            default=None,
            metadata={
                "name": "MIME",
                "type": "Attribute",
            },
        )
