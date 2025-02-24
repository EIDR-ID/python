from dataclasses import dataclass, field
from typing import Optional

from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.comp_obj_class_type import (
    CompObjClassType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.comp_obj_entry_type import (
    CompObjEntryType,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class CompObjType:
    class Meta:
        name = "CompObj-type"

    entry: list[CompObjEntryType] = field(
        default_factory=list,
        metadata={
            "name": "Entry",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    compilation_class: Optional[CompObjClassType] = field(
        default=None,
        metadata={
            "name": "CompilationClass",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
