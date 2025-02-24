from dataclasses import dataclass, field
from typing import Optional

from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.digital_asset_external_track_reference_type import (
    DigitalAssetExternalTrackReferenceType,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class ContainerTrackMetadataType:
    """
    Rather than restricting, validation rules could ignore any non-ID tracks.
    """

    class Meta:
        name = "ContainerTrackMetadata-type"

    external_track_reference: Optional[
        DigitalAssetExternalTrackReferenceType
    ] = field(
        default=None,
        metadata={
            "name": "ExternalTrackReference",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    internal_track_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "InternalTrackReference",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "max_length": 128,
        },
    )
