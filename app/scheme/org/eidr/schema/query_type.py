from dataclasses import dataclass, field
from typing import Optional

from    .asset_doitype import AssetDoitype

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class QueryType:
    class Meta:
        name = "queryType"

    id: Optional[AssetDoitype] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    expression: Optional[str] = field(
        default=None,
        metadata={
            "name": "Expression",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    page_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "PageNumber",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    page_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "PageSize",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    continuation_token: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContinuationToken",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    extended_family: Optional[bool] = field(
        default=None,
        metadata={
            "name": "extendedFamily",
            "type": "Attribute",
        },
    )
