from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class DigitalAssetVideoPicture360InitialType:
    class Meta:
        name = "DigitalAssetVideoPicture360Initial-type"

    heading_degrees: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "HeadingDegrees",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("360"),
        },
    )
    pitch_degrees: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PitchDegrees",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
            "min_inclusive": Decimal("-90"),
            "max_inclusive": Decimal("90"),
        },
    )
    roll_degress: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RollDegress",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
            "min_inclusive": Decimal("-180"),
            "max_inclusive": Decimal("180"),
        },
    )
