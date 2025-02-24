from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class DigitalAssetColorEncodingType:
    class Meta:
        name = "DigitalAssetColorEncoding-type"

    primaries: Optional[str] = field(
        default=None,
        metadata={
            "name": "Primaries",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
    transfer_function: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransferFunction",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
    color_differencing: Optional[str] = field(
        default=None,
        metadata={
            "name": "ColorDifferencing",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
