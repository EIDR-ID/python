from dataclasses import dataclass, field
from typing import Optional

from    app.scheme.org.eidr.schema.asset_doitype import AssetDoitype

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class GetLeafDescendantsType:
    class Meta:
        name = "getLeafDescendantsType"

    id: Optional[AssetDoitype] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    extended_family: Optional[bool] = field(
        default=None,
        metadata={
            "name": "extendedFamily",
            "type": "Attribute",
        },
    )
