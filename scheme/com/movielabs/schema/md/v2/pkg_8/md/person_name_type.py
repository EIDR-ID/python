from dataclasses import dataclass, field
from typing import Optional

from scheme.com.movielabs.schema.md.v2.pkg_8.md.string_and_language_type import (
    StringAndLanguageType,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class PersonNameType:
    """
    Restrict DisplayName and SortName to single occurrence, no space-only strings,
    no ; or :, minlength of 2.
    """

    class Meta:
        name = "PersonName-type"

    display_name: Optional[StringAndLanguageType] = field(
        default=None,
        metadata={
            "name": "DisplayName",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
    sort_name: Optional[StringAndLanguageType] = field(
        default=None,
        metadata={
            "name": "SortName",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    first_given_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "FirstGivenName",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    second_given_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SecondGivenName",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    family_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "FamilyName",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    suffix: Optional[str] = field(
        default=None,
        metadata={
            "name": "Suffix",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    moniker: Optional[str] = field(
        default=None,
        metadata={
            "name": "Moniker",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
