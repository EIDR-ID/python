from dataclasses import dataclass, field
from typing import Optional

from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.container_metadata_type import (
    ContainerMetadataType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.content_identifier_type import (
    ContentIdentifierType,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class ContainerMetadataWithIdType(ContainerMetadataType):
    class Meta:
        name = "ContainerMetadataWithID-type"

    container_id: Optional[ContentIdentifierType] = field(
        default=None,
        metadata={
            "name": "ContainerID",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
