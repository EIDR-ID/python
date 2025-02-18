from dataclasses import dataclass, field
from typing import Optional

from scheme.com.movielabs.schema.md.v2.pkg_8.md.container_specific_type import (
    ContainerSpecificType,
)
from scheme.com.movielabs.schema.md.v2.pkg_8.md.container_track_metadata_type import (
    ContainerTrackMetadataType,
)
from scheme.com.movielabs.schema.md.v2.pkg_8.md.hash_type import HashType
from scheme.com.movielabs.schema.md.v2.pkg_8.md.string_container_type import (
    StringContainerType,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class ContainerMetadataType:
    class Meta:
        name = "ContainerMetadata-type"

    type_value: Optional[StringContainerType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
    track: list[ContainerTrackMetadataType] = field(
        default_factory=list,
        metadata={
            "name": "Track",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "min_occurs": 1,
        },
    )
    hash: list[HashType] = field(
        default_factory=list,
        metadata={
            "name": "Hash",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    size: Optional[int] = field(
        default=None,
        metadata={
            "name": "Size",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    container_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContainerReference",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "max_length": 128,
        },
    )
    container_specific_metadata: Optional[ContainerSpecificType] = field(
        default=None,
        metadata={
            "name": "ContainerSpecificMetadata",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
