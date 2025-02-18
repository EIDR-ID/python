from dataclasses import dataclass, field
from typing import Optional

from scheme.com.movielabs.schema.md.v2.pkg_8.md.string_and_language_type import (
    StringAndLanguageType,
)
from scheme.com.movielabs.schema.md.v2.pkg_8.md.string_compilation_entry_class import (
    StringCompilationEntryClass,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class CompObjEntryType:
    class Meta:
        name = "CompObjEntry-type"

    display_name: Optional[StringAndLanguageType] = field(
        default=None,
        metadata={
            "name": "DisplayName",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    entry_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "EntryNumber",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "max_length": 8,
            "pattern": r"0|[1-9][0-9a-zA-Z]*([:,\-.,/][0-9a-zA-Z]+)?",
        },
    )
    entry_class: Optional[StringCompilationEntryClass] = field(
        default=None,
        metadata={
            "name": "EntryClass",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    content_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContentID",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
            "pattern": r"10\.5240/[\dA-F]{4}-[\dA-F]{4}-[\dA-F]{4}-[\dA-F]{4}-[\dA-F]{4}-[\dA-Z]|10\.5240/[\dA-F]{20}[\dA-Z]",
        },
    )
