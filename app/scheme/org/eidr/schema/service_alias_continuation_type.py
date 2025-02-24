from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class ServiceAliasContinuationType:
    class Meta:
        name = "serviceAliasContinuationType"

    last_aliased: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastAliased",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
            "pattern": r"10\.5239/[\dA-F]{4}-[\dA-F]{4}",
        },
    )
    target_of_last_aliased: Optional[str] = field(
        default=None,
        metadata={
            "name": "TargetOfLastAliased",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
            "pattern": r"10\.5239/[\dA-F]{4}-[\dA-F]{4}",
        },
    )
