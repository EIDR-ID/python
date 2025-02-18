from dataclasses import dataclass, field

from scheme.com.movielabs.schema.md.v2.pkg_8.md.container_metadata_type import (
    ContainerMetadataType,
)
from scheme.com.movielabs.schema.md.v2.pkg_8.md.digital_asset_metadata_type import (
    DigitalAssetMetadataType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class DigitalTracksType:
    class Meta:
        name = "digitalTracksType"

    track: list[DigitalAssetMetadataType] = field(
        default_factory=list,
        metadata={
            "name": "Track",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    container: list[ContainerMetadataType] = field(
        default_factory=list,
        metadata={
            "name": "Container",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
