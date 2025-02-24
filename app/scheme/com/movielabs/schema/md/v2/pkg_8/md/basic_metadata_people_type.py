from dataclasses import dataclass, field
from typing import Optional

from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.basic_metadata_job_type import (
    BasicMetadataJobType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.gender_type import GenderType
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.person_identifier_type import (
    PersonIdentifierType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.person_name_type import (
    PersonNameType,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class BasicMetadataPeopleType:
    class Meta:
        name = "BasicMetadataPeople-type"

    job: list[BasicMetadataJobType] = field(
        default_factory=list,
        metadata={
            "name": "Job",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "min_occurs": 1,
        },
    )
    name: Optional[PersonNameType] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
    identifier: list[PersonIdentifierType] = field(
        default_factory=list,
        metadata={
            "name": "Identifier",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    gender: Optional[GenderType] = field(
        default=None,
        metadata={
            "name": "Gender",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
