from dataclasses import dataclass, field
from typing import Optional

from scheme.com.movielabs.schema.md.v2.pkg_8.md.coordinate_earth_type import (
    CoordinateEarthType,
)
from scheme.com.movielabs.schema.md.v2.pkg_8.md.coordinate_other_type import (
    CoordinateOtherType,
)
from scheme.com.movielabs.schema.md.v2.pkg_8.md.region_type import RegionType

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class ContentRelatedToPlaceType:
    class Meta:
        name = "ContentRelatedToPlace-type"

    region: Optional[RegionType] = field(
        default=None,
        metadata={
            "name": "Region",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    address: Optional[str] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    earth_coordinate: Optional[CoordinateEarthType] = field(
        default=None,
        metadata={
            "name": "EarthCoordinate",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    other_coordinate: Optional[CoordinateOtherType] = field(
        default=None,
        metadata={
            "name": "OtherCoordinate",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    description: list["ContentRelatedToPlaceType.Description"] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    primary: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    fictional: Optional[bool] = field(
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
