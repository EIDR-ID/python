from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class CoordinateOtherType:
    class Meta:
        name = "CoordinateOther-type"

    coordinate: list["CoordinateOtherType.Coordinate"] = field(
        default_factory=list,
        metadata={
            "name": "Coordinate",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "min_occurs": 1,
        },
    )
    system: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )

    @dataclass
    class Coordinate:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        label: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )
