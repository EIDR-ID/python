from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlTime

from scheme.com.movielabs.schema.md.v2.pkg_8.md.content_sequence_info_type import (
    ContentSequenceInfoType,
)
from scheme.org.eidr.schema.asset_doitype import AssetDoitype
from scheme.org.eidr.schema.episode_class_type import EpisodeClassType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class EpisodeInfoType:
    """Episode must supply base object, ReferentType, StructuralType, ReleaseDate.

    If Episode is a child of a Season, it inherits the Season's
    TimeSlot. baseObjectData.ApproximateLength is used for the length of
    the episode baseObjectData.ResourceName is used to provide an
    episode title and is required, but may be submitted empty or
    replaced with a system-generated name under special circumstances.
    """

    class Meta:
        name = "episodeInfoType"

    parent: Optional[AssetDoitype] = field(
        default=None,
        metadata={
            "name": "Parent",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    sequence_info: Optional[ContentSequenceInfoType] = field(
        default=None,
        metadata={
            "name": "SequenceInfo",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    episode_class: list[EpisodeClassType] = field(
        default_factory=list,
        metadata={
            "name": "EpisodeClass",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    time_slot: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "TimeSlot",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
