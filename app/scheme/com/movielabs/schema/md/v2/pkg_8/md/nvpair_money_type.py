from dataclasses import dataclass, field
from typing import Optional

from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.money_type import MoneyType

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class NvpairMoneyType:
    class Meta:
        name = "NVPairMoney-type"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
    value: Optional[MoneyType] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
