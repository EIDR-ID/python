from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod

from scheme.com.movielabs.schema.md.v2.pkg_8.md.associated_org_type import (
    AssociatedOrgType,
)
from scheme.com.movielabs.schema.md.v2.pkg_8.md.region_type import RegionType

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class ReleaseHistoryType:
    class Meta:
        name = "ReleaseHistory-type"

    release_type: Optional["ReleaseHistoryType.ReleaseType"] = field(
        default=None,
        metadata={
            "name": "ReleaseType",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
    distr_territory: list[RegionType] = field(
        default_factory=list,
        metadata={
            "name": "DistrTerritory",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    date: Optional["ReleaseHistoryType.Date"] = field(
        default=None,
        metadata={
            "name": "Date",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    release_org: list[AssociatedOrgType] = field(
        default_factory=list,
        metadata={
            "name": "ReleaseOrg",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )

    @dataclass
    class ReleaseType:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        wide: Optional[bool] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Date:
        value: Optional[Union[XmlPeriod, XmlDate, XmlDateTime]] = field(
            default=None
        )
        scheduled: Optional[bool] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
