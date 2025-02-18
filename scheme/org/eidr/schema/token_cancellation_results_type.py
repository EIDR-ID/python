from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class TokenCancellationResultsType:
    class Meta:
        name = "tokenCancellationResultsType"

    cancelled_token_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "CancelledTokenCount",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    cancelled_token: list[str] = field(
        default_factory=list,
        metadata={
            "name": "CancelledToken",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
