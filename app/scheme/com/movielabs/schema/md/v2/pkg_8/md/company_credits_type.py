from dataclasses import dataclass, field
from typing import Optional

from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.region_type import RegionType

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class CompanyCreditsType:
    class Meta:
        name = "CompanyCredits-type"

    display_string: list["CompanyCreditsType.DisplayString"] = field(
        default_factory=list,
        metadata={
            "name": "DisplayString",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "min_occurs": 1,
        },
    )
    region: list[RegionType] = field(
        default_factory=list,
        metadata={
            "name": "Region",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    display_sequence: Optional[int] = field(
        default=None,
        metadata={
            "name": "DisplaySequence",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )

    @dataclass
    class DisplayString:
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
