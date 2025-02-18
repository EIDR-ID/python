from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class PersonIdentifierType:
    class Meta:
        name = "PersonIdentifier-type"

    identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "Identifier",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
    namespace: Optional[str] = field(
        default=None,
        metadata={
            "name": "Namespace",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
    reference_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReferenceLocation",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    scope: Optional["PersonIdentifierType.Scope"] = field(
        default=None,
        metadata={
            "name": "Scope",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )

    @dataclass
    class Scope:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        subscope: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
