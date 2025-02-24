from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class EidrurnType:
    class Meta:
        name = "EIDRURN-type"

    scope: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
