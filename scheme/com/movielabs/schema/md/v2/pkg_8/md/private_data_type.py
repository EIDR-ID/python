from dataclasses import dataclass, field
from typing import Optional

from scheme.com.movielabs.schema.md.v2.pkg_8.md.associated_org_type import (
    AssociatedOrgType,
)
from scheme.com.movielabs.schema.md.v2.pkg_8.md.hash_type import HashType
from scheme.com.movielabs.schema.md.v2.pkg_8.md.string_and_language_type import (
    StringAndLanguageType,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class PrivateDataType:
    class Meta:
        name = "PrivateData-type"

    encoding_agent: Optional[AssociatedOrgType] = field(
        default=None,
        metadata={
            "name": "EncodingAgent",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    description: Optional[StringAndLanguageType] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    hash: list[HashType] = field(
        default_factory=list,
        metadata={
            "name": "Hash",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "max_occurs": 8,
        },
    )
    size: Optional["PrivateDataType.Size"] = field(
        default=None,
        metadata={
            "name": "Size",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )

    @dataclass
    class Size:
        value: Optional[int] = field(
            default=None,
            metadata={
                "required": True,
            },
        )
        pad: Optional[int] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
