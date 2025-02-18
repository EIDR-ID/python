from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class DigitalAssetExternalTrackReferenceType:
    class Meta:
        name = "DigitalAssetExternalTrackReference-type"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"10\.5240/[\dA-F]{4}-[\dA-F]{4}-[\dA-F]{4}-[\dA-F]{4}-[\dA-F]{4}-[\dA-Z]|10\.5240/[\dA-F]{20}[\dA-Z]",
        },
    )
    namespace: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    track_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "trackReference",
            "type": "Attribute",
            "max_length": 128,
        },
    )
