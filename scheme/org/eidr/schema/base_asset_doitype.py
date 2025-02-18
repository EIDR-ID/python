from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class BaseAssetDoitype:
    class Meta:
        name = "baseAssetDOIType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
