from dataclasses import dataclass, field
from typing import Optional

from scheme.org.eidr.schema.asset_doitype import AssetDoitype
from scheme.org.eidr.schema.promotion_class_type import PromotionClassType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class PromotionInfoType:
    class Meta:
        name = "promotionInfoType"

    id: Optional[AssetDoitype] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    promotion_class: Optional[PromotionClassType] = field(
        default=None,
        metadata={
            "name": "PromotionClass",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
