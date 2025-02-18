from dataclasses import dataclass, field
from typing import Optional

from scheme.com.movielabs.schema.md.v2.pkg_8.md.color_type_type import (
    ColorTypeType,
)
from scheme.com.movielabs.schema.md.v2.pkg_8.md.made_for_region_type import (
    MadeForRegionType,
)
from scheme.org.eidr.schema.asset_doitype import AssetDoitype
from scheme.org.eidr.schema.edit_class_type import EditClassType
from scheme.org.eidr.schema.edit_use_type import EditUseType
from scheme.org.eidr.schema.usage_details_type import UsageDetailsType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class EditInfoType:
    """
    An edit must provide, rather than inherit, Description, ApproximateLength, and
    ReleaseDate on baseRegistrationData.
    """

    class Meta:
        name = "editInfoType"

    parent: Optional[AssetDoitype] = field(
        default=None,
        metadata={
            "name": "Parent",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    edit_use: Optional[EditUseType] = field(
        default=None,
        metadata={
            "name": "EditUse",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    edit_class: list[EditClassType] = field(
        default_factory=list,
        metadata={
            "name": "EditClass",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "max_occurs": 8,
        },
    )
    made_for_region: list[MadeForRegionType] = field(
        default_factory=list,
        metadata={
            "name": "MadeForRegion",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "max_occurs": 8,
        },
    )
    edit_details: list[UsageDetailsType] = field(
        default_factory=list,
        metadata={
            "name": "EditDetails",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "max_occurs": 8,
        },
    )
    color_type: Optional[ColorTypeType] = field(
        default=None,
        metadata={
            "name": "ColorType",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    three_d: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ThreeD",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
