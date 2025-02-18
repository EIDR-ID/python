from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class TokenCancellationRequestType:
    class Meta:
        name = "tokenCancellationRequestType"

    token: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Token",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "min_occurs": 1,
        },
    )
