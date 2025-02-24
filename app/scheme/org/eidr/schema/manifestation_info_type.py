from dataclasses import dataclass, field
from typing import Optional

from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.made_for_region_type import (
    MadeForRegionType,
)
from    .asset_doitype import AssetDoitype
from    .digital_tracks_type import DigitalTracksType
from    .film_tracks_type import FilmTracksType
from    .manifestation_class_type import (
    ManifestationClassType,
)
from    .tape_tracks_type import TapeTracksType
from    .usage_details_type import UsageDetailsType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class ManifestationInfoType:
    class Meta:
        name = "manifestationInfoType"

    parent: Optional[AssetDoitype] = field(
        default=None,
        metadata={
            "name": "Parent",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    manifestation_class: list[ManifestationClassType] = field(
        default_factory=list,
        metadata={
            "name": "ManifestationClass",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "min_occurs": 1,
            "max_occurs": 8,
        },
    )
    made_for_region: list[MadeForRegionType] = field(
        default_factory=list,
        metadata={
            "name": "MadeForRegion",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "max_occurs": 8,
        },
    )
    manifestation_details: list[UsageDetailsType] = field(
        default_factory=list,
        metadata={
            "name": "ManifestationDetails",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "max_occurs": 8,
        },
    )
    digital: Optional[DigitalTracksType] = field(
        default=None,
        metadata={
            "name": "Digital",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    film: Optional[FilmTracksType] = field(
        default=None,
        metadata={
            "name": "Film",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    tape: Optional[TapeTracksType] = field(
        default=None,
        metadata={
            "name": "Tape",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
