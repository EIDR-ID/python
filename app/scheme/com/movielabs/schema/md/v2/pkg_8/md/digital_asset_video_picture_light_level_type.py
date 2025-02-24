from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class DigitalAssetVideoPictureLightLevelType:
    class Meta:
        name = "DigitalAssetVideoPictureLightLevel-type"

    content_max: list["DigitalAssetVideoPictureLightLevelType.ContentMax"] = (
        field(
            default_factory=list,
            metadata={
                "name": "ContentMax",
                "type": "Element",
                "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            },
        )
    )
    frame_average_max: list[
        "DigitalAssetVideoPictureLightLevelType.FrameAverageMax"
    ] = field(
        default_factory=list,
        metadata={
            "name": "FrameAverageMax",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )

    @dataclass
    class ContentMax:
        value: Optional[int] = field(
            default=None,
            metadata={
                "required": True,
            },
        )
        interpretation: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class FrameAverageMax:
        value: Optional[int] = field(
            default=None,
            metadata={
                "required": True,
            },
        )
        interpretation: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
