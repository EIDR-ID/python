from dataclasses import dataclass, field
from typing import Optional

from scheme.com.movielabs.schema.md.v2.pkg_8.md.compliance_type import (
    ComplianceType,
)
from scheme.com.movielabs.schema.md.v2.pkg_8.md.content_identifier_type import (
    ContentIdentifierType,
)
from scheme.com.movielabs.schema.md.v2.pkg_8.md.digital_asset_metadata_type import (
    DigitalAssetMetadataType,
)
from scheme.com.movielabs.schema.md.v2.pkg_8.md.private_data_type import (
    PrivateDataType,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class DigitalAssetAncillaryDataType:
    class Meta:
        name = "DigitalAssetAncillaryData-type"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
        },
    )
    sub_type: list[str] = field(
        default_factory=list,
        metadata={
            "name": "SubType",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    base_track_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "BaseTrackID",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    base_track_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "BaseTrackReference",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "max_length": 128,
        },
    )
    base_track_identifier: list[ContentIdentifierType] = field(
        default_factory=list,
        metadata={
            "name": "BaseTrackIdentifier",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    track_metadata: Optional[DigitalAssetMetadataType] = field(
        default=None,
        metadata={
            "name": "TrackMetadata",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    combined_metadata: Optional[DigitalAssetMetadataType] = field(
        default=None,
        metadata={
            "name": "CombinedMetadata",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    compliance: list[ComplianceType] = field(
        default_factory=list,
        metadata={
            "name": "Compliance",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    private: Optional[PrivateDataType] = field(
        default=None,
        metadata={
            "name": "Private",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
