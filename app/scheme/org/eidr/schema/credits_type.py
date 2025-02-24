from dataclasses import dataclass, field

from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.person_name_type import (
    PersonNameType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class CreditsType:
    class Meta:
        name = "creditsType"

    director: list[PersonNameType] = field(
        default_factory=list,
        metadata={
            "name": "Director",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "max_occurs": 2,
        },
    )
    actor: list[PersonNameType] = field(
        default_factory=list,
        metadata={
            "name": "Actor",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "max_occurs": 4,
        },
    )
