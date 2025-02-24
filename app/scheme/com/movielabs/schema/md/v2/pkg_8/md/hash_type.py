from dataclasses import dataclass, field
from typing import Optional

from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.string_hash_method import (
    StringHashMethod,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class HashType:
    class Meta:
        name = "Hash-type"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[0-9a-fA-F]+",
        },
    )
    method: Optional[StringHashMethod] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
