from dataclasses import dataclass, field
from typing import Optional

from scheme.com.movielabs.schema.md.v2.pkg_8.md.basic_metadata_character_type import (
    BasicMetadataCharacterType,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class BasicMetadataJobType:
    class Meta:
        name = "BasicMetadataJob-type"

    job_function: Optional["BasicMetadataJobType.JobFunction"] = field(
        default=None,
        metadata={
            "name": "JobFunction",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
    job_display: list["BasicMetadataJobType.JobDisplay"] = field(
        default_factory=list,
        metadata={
            "name": "JobDisplay",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    billing_block_order: Optional["BasicMetadataJobType.BillingBlockOrder"] = (
        field(
            default=None,
            metadata={
                "name": "BillingBlockOrder",
                "type": "Element",
                "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            },
        )
    )
    character: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Character",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    character_info: list[BasicMetadataCharacterType] = field(
        default_factory=list,
        metadata={
            "name": "CharacterInfo",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    guest: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Guest",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )

    @dataclass
    class JobFunction:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        scheme: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class JobDisplay:
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

    @dataclass
    class BillingBlockOrder:
        value: Optional[int] = field(
            default=None,
            metadata={
                "required": True,
            },
        )
        top_billed: Optional[bool] = field(
            default=None,
            metadata={
                "name": "topBilled",
                "type": "Attribute",
            },
        )
