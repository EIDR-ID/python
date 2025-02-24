from dataclasses import dataclass, field
from typing import Optional

from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.region_type import RegionType

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class ContentRatingDetailType:
    class Meta:
        name = "ContentRatingDetail-type"

    region: Optional[RegionType] = field(
        default=None,
        metadata={
            "name": "Region",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
    system: Optional[str] = field(
        default=None,
        metadata={
            "name": "System",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
    reason: list["ContentRatingDetailType.Reason"] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    link_to_logo: list["ContentRatingDetailType.LinkToLogo"] = field(
        default_factory=list,
        metadata={
            "name": "LinkToLogo",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    description: list["ContentRatingDetailType.Description"] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )

    @dataclass
    class Reason:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        value_attribute: Optional[str] = field(
            default=None,
            metadata={
                "name": "value",
                "type": "Attribute",
            },
        )

    @dataclass
    class LinkToLogo:
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
        authoritative: Optional[bool] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        origin: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
