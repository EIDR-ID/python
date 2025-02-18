from dataclasses import dataclass, field
from typing import Optional

from scheme.com.movielabs.schema.md.v2.pkg_8.md.string_compilation_compilation_class import (
    StringCompilationCompilationClass,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class CompObjClassType:
    class Meta:
        name = "CompObjClass-type"

    value: Optional[StringCompilationCompilationClass] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    has_other_inclusions: Optional[bool] = field(
        default=None,
        metadata={
            "name": "hasOtherInclusions",
            "type": "Attribute",
        },
    )
