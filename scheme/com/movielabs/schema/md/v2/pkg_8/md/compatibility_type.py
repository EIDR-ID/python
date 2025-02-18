from dataclasses import dataclass, field
from typing import Optional

from scheme.com.movielabs.schema.md.v2.pkg_8.md.terms_type import TermsType

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class CompatibilityType:
    """
    :ivar spec_version: Version of the specification to which this
        document is authored
    :ivar system:
    :ivar profile:
    :ivar validator_parameter:
    """

    class Meta:
        name = "Compatibility-type"

    spec_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "SpecVersion",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
    system: list[str] = field(
        default_factory=list,
        metadata={
            "name": "System",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    profile: Optional["CompatibilityType.Profile"] = field(
        default=None,
        metadata={
            "name": "Profile",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
    validator_parameter: list[TermsType] = field(
        default_factory=list,
        metadata={
            "name": "ValidatorParameter",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )

    @dataclass
    class Profile:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        sub_profile: Optional[str] = field(
            default=None,
            metadata={
                "name": "subProfile",
                "type": "Attribute",
            },
        )
