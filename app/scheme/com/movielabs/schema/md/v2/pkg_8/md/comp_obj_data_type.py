from dataclasses import dataclass, field
from typing import Optional

from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.comp_obj_type import (
    CompObjType,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class CompObjDataType(CompObjType):
    class Meta:
        name = "CompObjData-type"

    display_name: list["CompObjDataType.DisplayName"] = field(
        default_factory=list,
        metadata={
            "name": "DisplayName",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    comp_obj_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CompObjID",
            "type": "Attribute",
        },
    )

    @dataclass
    class DisplayName:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        language: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
