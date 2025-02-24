from dataclasses import dataclass, field
from typing import Optional

from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.associated_org_type import (
    AssociatedOrgType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.string_and_language_type import (
    StringAndLanguageType,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class ContainerSpecificType:
    class Meta:
        name = "ContainerSpecific-type"

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
