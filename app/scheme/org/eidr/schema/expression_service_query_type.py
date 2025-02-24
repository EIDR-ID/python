from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class ExpressionServiceQueryType:
    class Meta:
        name = "expressionServiceQueryType"

    expression: Optional[str] = field(
        default=None,
        metadata={
            "name": "Expression",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    page_number: int = field(
        default=1,
        metadata={
            "name": "PageNumber",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    page_size: int = field(
        default=20,
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
