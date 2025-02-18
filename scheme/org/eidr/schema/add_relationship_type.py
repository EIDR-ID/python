from dataclasses import dataclass, field
from typing import Optional

from scheme.org.eidr.schema.alternate_content_info_type import (
    AlternateContentInfoType,
)
from scheme.org.eidr.schema.asset_doitype import AssetDoitype
from scheme.org.eidr.schema.composite_info_type import CompositeInfoType
from scheme.org.eidr.schema.packaging_info_type import PackagingInfoType
from scheme.org.eidr.schema.promotion_info_type import PromotionInfoType
from scheme.org.eidr.schema.supplemental_content_info_type import (
    SupplementalContentInfoType,
)
from scheme.org.eidr.schema.target_relationship_type import (
    TargetRelationshipType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class AddRelationshipType:
    class Meta:
        name = "addRelationshipType"

    id: Optional[AssetDoitype] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    composite_info: Optional[CompositeInfoType] = field(
        default=None,
        metadata={
            "name": "CompositeInfo",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    promotion_info: Optional[PromotionInfoType] = field(
        default=None,
        metadata={
            "name": "PromotionInfo",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    supplemental_content_info: Optional[SupplementalContentInfoType] = field(
        default=None,
        metadata={
            "name": "SupplementalContentInfo",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    alternate_content_info: Optional[AlternateContentInfoType] = field(
        default=None,
        metadata={
            "name": "AlternateContentInfo",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    packaging_info: Optional[PackagingInfoType] = field(
        default=None,
        metadata={
            "name": "PackagingInfo",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    type_value: Optional[TargetRelationshipType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )
