from dataclasses import dataclass, field
from typing import Optional

from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.comp_obj_type import (
    CompObjType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.digital_asset_interactive_base_data_type import (
    DigitalAssetInteractiveBaseDataType,
)
from    .alternate_content_info_type import (
    AlternateContentInfoType,
)
from    .clip_info_type import ClipInfoType
from    .composite_info_type import CompositeInfoType
from    .edit_info_type import EditInfoType
from    .episode_info_type import EpisodeInfoType
from    .manifestation_info_type import (
    ManifestationInfoType,
)
from    .packaging_info_type import PackagingInfoType
from    .promotion_info_type import PromotionInfoType
from   .season_info_type import SeasonInfoType
from    .series_info_type import SeriesInfoType
from    .supplemental_content_info_type import (
    SupplementalContentInfoType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class ExtraObjectMetadataType:
    """Metadata for child objects and derived objects.

    This schema enforces the following rules for what extra metadata can
    be present ((0 or 1 of compilation, season, series, interactive
    material, episode, episode+composite, or composite) OR (0 or 1 of
    Edit,Manifestation, or Clip)) AND (0 or more of each of Promotion,
    Supplement, AlternateContent, Packaging)
    """

    class Meta:
        name = "extraObjectMetadataType"

    compilation_info: Optional[CompObjType] = field(
        default=None,
        metadata={
            "name": "CompilationInfo",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    season_info: Optional[SeasonInfoType] = field(
        default=None,
        metadata={
            "name": "SeasonInfo",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    series_info: Optional[SeriesInfoType] = field(
        default=None,
        metadata={
            "name": "SeriesInfo",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    interactive_material_info: Optional[
        DigitalAssetInteractiveBaseDataType
    ] = field(
        default=None,
        metadata={
            "name": "InteractiveMaterialInfo",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    episode_info: Optional[EpisodeInfoType] = field(
        default=None,
        metadata={
            "name": "EpisodeInfo",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    composite_info: list[CompositeInfoType] = field(
        default_factory=list,
        metadata={
            "name": "CompositeInfo",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    edit_info: Optional[EditInfoType] = field(
        default=None,
        metadata={
            "name": "EditInfo",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    manifestation_info: Optional[ManifestationInfoType] = field(
        default=None,
        metadata={
            "name": "ManifestationInfo",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    clip_info: Optional[ClipInfoType] = field(
        default=None,
        metadata={
            "name": "ClipInfo",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    promotion_info: list[PromotionInfoType] = field(
        default_factory=list,
        metadata={
            "name": "PromotionInfo",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    supplemental_content_info: list[SupplementalContentInfoType] = field(
        default_factory=list,
        metadata={
            "name": "SupplementalContentInfo",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    alternate_content_info: list[AlternateContentInfoType] = field(
        default_factory=list,
        metadata={
            "name": "AlternateContentInfo",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    packaging_info: list[PackagingInfoType] = field(
        default_factory=list,
        metadata={
            "name": "PackagingInfo",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
