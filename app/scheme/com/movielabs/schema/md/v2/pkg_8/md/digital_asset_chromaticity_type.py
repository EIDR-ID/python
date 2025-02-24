from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class DigitalAssetChromaticityType:
    class Meta:
        name = "DigitalAssetChromaticity-type"

    chromaticity_ciex: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ChromaticityCIEx",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
    chromaticity_ciey: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ChromaticityCIEy",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
