from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class DigitalAssetVideoPictureHdrplaybackInfoType:
    class Meta:
        name = "DigitalAssetVideoPictureHDRPlaybackInfo-type"

    sdrdownconversion: Optional[str] = field(
        default=None,
        metadata={
            "name": "SDRDownconversion",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
