from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class MoneyType:
    class Meta:
        name = "Money-type"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    currency: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
