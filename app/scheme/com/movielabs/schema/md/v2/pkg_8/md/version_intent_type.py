from dataclasses import dataclass, field
from typing import Optional

from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.audience_type import (
    AudienceType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.region_type import RegionType
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.terms_type import TermsType

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class VersionIntentType:
    class Meta:
        name = "VersionIntent-type"

    audience: Optional[AudienceType] = field(
        default=None,
        metadata={
            "name": "Audience",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    description: list["VersionIntentType.Description"] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    edit_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "EditUse",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    edit_class: list[str] = field(
        default_factory=list,
        metadata={
            "name": "EditClass",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    made_for_region: Optional[RegionType] = field(
        default=None,
        metadata={
            "name": "MadeForRegion",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    terms: list[TermsType] = field(
        default_factory=list,
        metadata={
            "name": "Terms",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )

    @dataclass
    class Description:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        language: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
