from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class DigitalAssetAudioLoudnessType:
    class Meta:
        name = "DigitalAssetAudioLoudness-type"

    level: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Level",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    deviation: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    leq_m: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "LeqM",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    compliance: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Compliance",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
