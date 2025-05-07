from typing import List, TypedDict, Optional, Union, Any

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.models.datatype import XmlPeriod, XmlDate, XmlTime, XmlDuration

from app.scheme.com.movielabs.schema.md.v2.pkg_8.md import StringCompilationCompilationClass, StringInteractiveType, \
    StringInteractiveFormatType, ComplexSequenceInfoDistributionNumber, MadeForRegionType, ColorTypeType, \
    StringAudioType, DigitalAssetAudioEncodingType, StringAudioEncCodec, StringAudioEncVbr, \
    StringAudioEncChannelMapping, StringAssociatedOrgRole, StringHashMethod, StringVideoType, StringVideoPictureFormat, \
    StringVideoEncCodec, StringVideoEncMprofile, StringVideoEncMlevel, StringVideoEncVbr, StringVideoPicPixelAspect, \
    DigitalAssetVideoPictureFrameRateType, StringVideoPicFrameRateMultiplier, StringVideoPicFrameRateTimecode, \
    DigitalAssetVideoPictureProgressiveType, StringVideoPicProgressiveScanOrder, StringVideoPicColorimetry, \
    StringVideoPicColorSampling, StringVideoPicType3D, StringVideoSubLangType, StringCardsetListType, \
    DigitalAssetCardsetType, StringCardsetType, StringSubtitleType, StringSubtitleFormatType, StringSubtitleFormat, \
    StringInteractiveEncRuntimeEnvironment, StringContainerType, ContainerSpecificType, StringOrgNameIdType

config = ParserConfig()
context = XmlContext()
parser = XmlParser(context=context, config=config)
ns = {"": "http://www.eidr.org/schema"}

from app.scheme.org.eidr.schema import FullObjectInfoType, SeasonClassType, AssetDoitype, SeriesClassType, \
    EpisodeClassType, CompositeClassType, AlternateIdrelationType, ComponentsModeType, EditUseType, EditClassType, \
    UsageDetailsType, PromotionClassType, SupplementalContentClassType, AlternateContentInfoType, PackagingInfoType, \
    ManifestationClassType, ExtraObjectMetadataType, TitleClassType, DoiModeRestricted, LanguageTrackTypeType, Service, \
    ServiceResolutionType, Party, PartyResolutionType
from app.scheme.org.eidr.schema.base_object_info_type import BaseObjectInfoType, AssociatedOrgType, \
    CreationStructuralType, ModeType, ReferentType, StatusType, TitleType


class NameAndLanguageDict(TypedDict):
    name: str
    language: str


class NameDict(TypedDict):
    display_name: NameAndLanguageDict
    sort_name: NameAndLanguageDict
    first_given_name: Optional[str]
    second_given_name: Optional[str]
    family_name: Optional[str]
    suffix: Optional[str]
    moniker: Optional[str]








class CreditsDict(TypedDict):
    director: List[NameDict]
    actor: List[NameDict]


class AdministratorsDict(TypedDict):
    registrant: str
    metadata_authority: List[str]


class TitleDict(TypedDict):
    value: str  # max length 256
    title_class: Optional[str | TitleClassType]
    lang: Optional[str]
    system_generated: Optional[bool]


class LanguageDict(TypedDict):
    value: str
    mode: Optional[str | DoiModeRestricted]
    type_value: Optional[str | LanguageTrackTypeType]


class BaseObjectMeta:
    obj: BaseObjectInfoType | None = None
    structural_type: str | CreationStructuralType = None  # Mandatory
    mode: str | ModeType = None  # Mandatory
    referent_type: str | ReferentType = None  # Mandatory
    resource_name: str = None  # Mandatory
    administrators: AdministratorsDict = None
    alternate_resource_name: List[TitleDict] | None = None
    original_language: List[LanguageDict] = []
    version_language: List[LanguageDict] = []
    associated_org: List[StringAssociatedOrgRole] = []
    release_date: XmlDate | XmlPeriod = None  # Mandatory
    country_of_origin: List[str] = None
    status: StatusType | None = None
    approximate_length: XmlDuration | None = None
    alternate_id: List[str] = None
    credits: CreditsDict | None = None
    registrant_extra: str | None = None
    description: str | None = None

    @classmethod
    def from_string(cls, res_str: str):
        return cls(parser.from_string(res_str, BaseObjectInfoType, ns))

    def __init__(self, obj: BaseObjectInfoType):
        self.obj = obj
        self.id = obj.id.value
        self.structural_type = obj.structural_type
        self.mode = obj.mode
        self.referent_type = obj.referent_type
        self.resource_name = obj.resource_name.value
        self.administrators = AdministratorsDict(
            registrant=obj.administrators.registrant.value,
            metadata_authority=[auth.value for auth in obj.administrators.metadata_authority]
        )
        self.alternate_resource_name = [TitleDict(
            value=name.value,
            title_class=name.title_class.value if name.title_class else None,
            lang=name.lang,
            system_generated=name.system_generated
        ) for name in obj.alternate_resource_name]
        self.original_language = [LanguageDict(
            value=lang.value,
            mode=lang.mode,
            type_value=lang.type_value
        ) for lang in obj.original_language]
        self.version_language = [LanguageDict(
            value=lang.value,
            mode=lang.mode,
            type_value=lang.type_value
        ) for lang in obj.version_language]
        self.associated_org = [org.role for org in obj.associated_org]  # TODO: Full dict here?
        self.release_date = obj.release_date
        self.country_of_origin = [country.value for country in obj.country_of_origin]
        self.status = obj.status
        self.approximate_length = obj.approximate_length
        self.alternate_id = [alt.value for alt in obj.alternate_id]
        self.credits = None if obj.credits is None else CreditsDict(
            actor=[] if len(obj.credits.actor) <= 0 else [NameDict(
                display_name=NameAndLanguageDict(name=name.display_name.value or None,
                                                 language=name.display_name.language or None),
                sort_name=NameAndLanguageDict(name=name.sort_name.value,
                                              language=name.sort_name.language) if name.sort_name else None,
                first_given_name=name.first_given_name or None,
                second_given_name=name.second_given_name or None,
                family_name=name.family_name or None,
                suffix=name.suffix or None,
                moniker=name.moniker or None
            ) for name in obj.credits.actor],
            director=[] if len(obj.credits.director) <= 0 else [NameDict(
                display_name=NameAndLanguageDict(name=name.display_name.value or None,
                                                 language=name.display_name.language or None),
                sort_name=NameAndLanguageDict(name=name.sort_name.value if name.sort_name is not None else None,
                                              language=name.sort_name.language if name.sort_name is not None else None),
                first_given_name=name.first_given_name or None,
                second_given_name=name.second_given_name or None,
                family_name=name.family_name or None,
                suffix=name.suffix or None,
                moniker=name.moniker or None
            ) for name in obj.credits.director]
        )

        self.registrant_extra = obj.registrant_extra
        self.description = None if obj.description is None else obj.description.value

    def __repr__(self):
        dict = self.__dict__.copy()
        del dict["obj"]
        return str(dict)


from app.scheme.com.movielabs.schema.md.v2.pkg_8.md.comp_obj_class_type import CompObjClassType
from app.scheme.com.movielabs.schema.md.v2.pkg_8.md.comp_obj_entry_type import CompObjEntryType, \
    StringCompilationEntryClass, StringAndLanguageType


class StringAndLanguageDict(TypedDict):
    value: str
    language: Optional[str]


# Compilation Info

class CompObjClassDict(TypedDict):
    value: Optional[StringCompilationCompilationClass | str]
    has_other_inclusions: Optional[bool]


class CompObjEntryDict(TypedDict):
    display_name: StringAndLanguageDict
    entry_number: Optional[str]
    entry_class: StringCompilationEntryClass | str
    content_id: Optional[str]


class CompObjectDict(TypedDict):
    entry: list[CompObjEntryDict]
    compilation_class: Optional[CompObjClassDict]


# Season Info
class SeasonInfoDict(TypedDict):
    parent: str | AssetDoitype
    end_date: Optional[str | Union[XmlPeriod, XmlDate]]
    season_class: List[str | SeasonClassType]
    number_required: Optional[bool]
    date_required: Optional[bool]
    original_title_required: Optional[bool]
    sequence_number: Optional[int]


# Series Info
class SeriesInfoDict(TypedDict):
    end_date: Optional[str | Union[XmlPeriod, XmlDate]]
    series_class: Optional[str | SeriesClassType]
    number_required: Optional[bool]
    date_required: Optional[bool]
    original_title_required: Optional[bool]


# Interactive material
class DigitalAssetInteractiveBaseDataDict(TypedDict):
    type_value: Optional[str | StringInteractiveType]
    format_type: Optional[str | StringInteractiveFormatType]
    language: Optional[str]


# Episode Info

class ComplexSequenceInfoDict(TypedDict):
    value: str
    domain: Optional[str]  # pattern: r"[\S]+[.][\S]+"


class ComplexSequenceInfoDistributionNumberDict(ComplexSequenceInfoDict):
    # value pattern: r"0|[1-9][0-9a-zA-Z]*([:/\-.,][0-9a-zA-Z]+)?"
    pass


class ComplexSequenceInfoHouseSequenceDict(ComplexSequenceInfoDict):
    # value pattern: r"[0-9a-zA-Z:/\-.,]+"
    pass


class ComplexSequenceInfoAlternateNumberDict(ComplexSequenceInfoDict):
    # value pattern: r"[0-9a-zA-Z]+([:/\-.,][0-9a-zA-Z]+)*"
    pass


class ContentSequenceInfoDict(TypedDict):
    distribution_number: Optional[ComplexSequenceInfoDistributionNumberDict]
    house_sequence: Optional[ComplexSequenceInfoHouseSequenceDict]
    alternate_number: List[ComplexSequenceInfoAlternateNumberDict]


class EpisodeInfoDict(TypedDict):
    parent: str | AssetDoitype
    sequence_info: Optional[ContentSequenceInfoDict]
    episode_class: List[str | EpisodeClassType]
    time_slot: Optional[str | XmlTime]


# Composite Info

class AlternateIdDict(TypedDict):
    value: str  # max length 1024
    relation: Optional[str | AlternateIdrelationType]


class CompositeElementDict(TypedDict):
    id: Optional[str | AssetDoitype]
    other_id: Optional[AlternateIdDict]
    source_start: Optional[str | XmlDuration]
    source_duration: Optional[str | XmlDuration]
    components_mode: Optional[str | ComponentsModeType]
    dest_start: Optional[str | XmlDuration]
    dest_duration: Optional[str | XmlDuration]
    description: Optional[str]


class CompositeInfoDict(TypedDict):
    composite_class: Optional[str | CompositeClassType]
    element: List[CompositeElementDict]


# Edit Info

class UsageDetailsDict(TypedDict):
    value: str  # max length 128
    domain: Optional[str]  # pattern: r"[\S]+[.][\S]+"


class EditInfoDict(TypedDict):
    parent: Optional[str | AssetDoitype]
    edit_use: Optional[str | EditUseType]
    edit_class: List[str | EditClassType]
    made_for_region: List[str | MadeForRegionType]
    edit_details: List[UsageDetailsDict]
    color_type: Optional[str | ColorTypeType]
    three_d: Optional[bool]


# Manifestation Info

class DigitalAssetWatermarkDict(TypedDict):
    vendor: Optional[str]
    product_and_version_id: Optional[str]
    data: Optional[str]
    guaranteed_absent: Optional[bool]


class DigitalAssetAudioEncodingDict(TypedDict):
    codec: Optional[str | StringAudioEncCodec]
    codec_type: List[str]  # pattern r"(mpeg4ra|IANA|rfc4281):.{1,128}"
    bitrate_max: Optional[int]
    bitrate_average: Optional[int]
    vbr: Optional[str | StringAudioEncVbr]
    sample_rate: Optional[int]
    sample_bit_depth: Optional[int]
    channel_mapping: Optional[str | StringAudioEncChannelMapping]
    watermark: List[DigitalAssetWatermarkDict]
    actual_length: Optional[str | XmlDuration]


class DigitalAssetAudioLanguageDict(TypedDict):
    value: str
    dubbed: Optional[bool]


class AssociatedOrgDict(TypedDict):  # Redundant wrapper for StringAssociatedOrgRole
    role: Optional[str | StringAssociatedOrgRole]


class HashDict(TypedDict):
    value: str  # pattern r"[0-9a-fA-F]+"
    method: Optional[str | StringHashMethod]


class SizeDict(TypedDict):
    value: int
    pad: Optional[int]


class PrivateDataDict(TypedDict):
    encoding_agent: Optional[str | AssociatedOrgDict | StringAssociatedOrgRole]
    description: Optional[StringAndLanguageDict]
    hash: List[HashDict]
    size: Optional[SizeDict]


class DigitalAssetAudioDict(TypedDict):
    description: Optional[str]
    type_value: Optional[str | StringAudioType]
    encoding: Optional[DigitalAssetAudioEncodingDict]
    language: Optional[DigitalAssetAudioLanguageDict]
    channel: Optional[str]
    track_reference: Optional[str]
    private: Optional[PrivateDataDict]


class DigitalAssetVideoEncodingDict(TypedDict):
    codec: Optional[str | StringVideoEncCodec]
    codec_type: List[str]  # pattern r"(mpeg4ra|IANA):.{1,128}"
    mpegprofile: Optional[str | StringVideoEncMprofile]
    mpeglevel: Optional[str | StringVideoEncMlevel]
    bitrate_max: Optional[int]
    bit_rate_average: Optional[int]
    vbr: Optional[str | StringVideoEncVbr]
    watermark: List[DigitalAssetWatermarkDict]
    actual_length: Optional[str | XmlDuration]


class DigitalAssetVideoPictureFrameRateDict(TypedDict):
    value: Optional[int]
    multiplier: Optional[str | StringVideoPicFrameRateMultiplier]
    timecode: Optional[str | StringVideoPicFrameRateTimecode]


class DigitalAssetVideoPictureProgressiveDict(TypedDict):
    value: Optional[bool]
    scan_order: Optional[str | StringVideoPicProgressiveScanOrder]


class DigitalAssetVideoPictureDict(TypedDict):
    aspect_ratio: Optional[str]
    pixel_aspect: Optional[str | StringVideoPicPixelAspect]
    width_pixels: Optional[int]
    height_pixels: Optional[int]
    active_width_pixels: Optional[int]
    active_height_pixels: Optional[int]
    frame_rate: Optional[DigitalAssetVideoPictureFrameRateDict]
    progressive: Optional[DigitalAssetVideoPictureProgressiveDict]
    color_subsampling: Optional[str | StringVideoPicColorSampling]
    colorimetry: Optional[str | StringVideoPicColorimetry]
    type3_d: Optional[str | StringVideoPicType3D]


class DigitalAssetVideoSubtitleLanguageDict(TypedDict):
    value: str
    closed: Optional[bool]
    type_value: Optional[str | StringVideoSubLangType]


class DigitalAssetCardsetDict(TypedDict):
    type_value: List[str | StringCardsetType]
    description: Optional[str]  # max length 128
    sequence: Optional[int]


class DigitalAssetCardsetListDict(TypedDict):
    type_value: List[str | StringCardsetListType]
    region: List[str | MadeForRegionType]
    cardset: List[DigitalAssetCardsetDict]


class DigitalAssetVideoDataDict(TypedDict):
    description: Optional[str]
    type_value: Optional[str | StringVideoType]
    encoding: Optional[DigitalAssetVideoEncodingDict]
    picture: Optional[DigitalAssetVideoPictureDict]
    color_type: Optional[str | ColorTypeType]
    picture_format: Optional[str | StringVideoPictureFormat]
    subtitle_language: List[DigitalAssetVideoSubtitleLanguageDict]
    signed_language: Optional[str]
    cardset_list: Optional[DigitalAssetCardsetListDict]
    track_reference: Optional[str]  # max length 128
    private: Optional[PrivateDataDict]


class DigitalAssetSubtitleFormatDict(TypedDict):
    value: Optional[str | StringSubtitleFormat]
    sdimage: Optional[bool]
    hdimage: Optional[bool]


class DigitalAssetSubtitleDataDict(TypedDict):
    format: Optional[DigitalAssetSubtitleFormatDict]
    description: Optional[str]
    type_value: List[str | StringSubtitleType]
    format_type: Optional[str | StringSubtitleFormatType]
    language: Optional[str]
    cardset_list: Optional[DigitalAssetCardsetListDict]
    track_reference: Optional[str]  # max length 128
    private: Optional[PrivateDataDict]


class DigitalAssetInteractiveEncodingDict(TypedDict):
    runtime_environment: Optional[str | StringInteractiveEncRuntimeEnvironment]
    first_version: Optional[str]  # max length 64
    last_version: Optional[str]  # max length 64


class DigitalAssetInteractiveDataDict(TypedDict):
    type_value: Optional[str | StringInteractiveType]
    format_type: Optional[str | StringInteractiveFormatType]
    language: Optional[str]
    encoding: List[DigitalAssetInteractiveEncodingDict]
    track_reference: Optional[str]  # max length 128
    private: Optional[PrivateDataDict]


class DigitalAssetMetadataDict(TypedDict):
    audio: Optional[DigitalAssetAudioDict]
    video: Optional[DigitalAssetVideoDataDict]
    subtitle: Optional[DigitalAssetSubtitleDataDict]
    interactive: Optional[DigitalAssetInteractiveDataDict]


class DigitalAssetExternalTrackReferenceDict(TypedDict):
    value: str  # pattern r"10\.5240/[\dA-F]{4}-[\dA-F]{4}-[\dA-F]{4}-[\dA-F]{4}-[\dA-F]{4}-[\dA-Z]|10\.5240/[\dA-F]{20}[\dA-Z]"
    namespace: Optional[str]
    location: Optional[str]
    track_reference: Optional[str]  # max length 128


class ContainerTrackMetadataDict(TypedDict):
    external_track_reference: Optional[DigitalAssetExternalTrackReferenceDict]
    internal_track_reference: Optional[str]  # max length 128


class ContainerSpecificDict(TypedDict):
    coding_agent: Optional[AssociatedOrgDict]
    description: Optional[StringAndLanguageDict]


class ContainerMetadataDict(TypedDict):
    type_value: Optional[str | StringContainerType]
    track: List[ContainerTrackMetadataDict]
    hash: List[HashDict]
    size: Optional[int]
    container_reference: Optional[str]  # max length 128
    container_specific_metadata: Optional[ContainerSpecificDict]


class DigitalTracksDict(TypedDict):
    track: List[DigitalAssetMetadataDict]
    container: List[ContainerMetadataDict]


class FilmTracksDict(TypedDict):
    pass  # Nothing?


class TapeTracksDict(TypedDict):
    pass  # Nothing as well?


class ManifestationInfoDict(TypedDict):
    parent: str | AssetDoitype
    manifestation_class: List[str | ManifestationClassType]
    made_for_region: List[str | MadeForRegionType]
    manifestation_details: List[UsageDetailsDict]
    digital: Optional[DigitalTracksDict]
    film: Optional[FilmTracksDict]
    tape: Optional[TapeTracksDict]


# Clip Info
class ClipInfoDict(TypedDict):
    parent: str | AssetDoitype
    components_mode: str | ComponentsModeType
    start: Optional[str | XmlDuration]
    duration: List[str | XmlDuration]


# Promotion Info
class PromotionInfoDict(TypedDict):
    id: str | AssetDoitype
    promotion_class: Optional[str | PromotionClassType]


# Supplemental Content Info
class SupplementalContentInfoDict(TypedDict):
    id: str | AssetDoitype
    supplemental_content_class: Optional[str | SupplementalContentClassType]


# Alternate Content Info
class AlternateContentInfoDict(TypedDict):
    id: str | AssetDoitype
    alternate_content_class: Optional[str | AlternateContentInfoType]


# Packaging Info
class PackagingInfoDict(TypedDict):
    id: str | AssetDoitype
    packaging_class: Optional[str | PackagingInfoType]


class ExtraObjectMeta:
    compilation_info: Optional[CompObjectDict]
    season_info: Optional[SeasonInfoDict]
    series_info: Optional[SeriesInfoDict]
    interactive_material_info: Optional[DigitalAssetInteractiveBaseDataDict]
    episode_info: Optional[EpisodeInfoDict]
    composite_info: List[CompositeInfoDict]
    edit_info: Optional[EditInfoDict]
    manifestation_info: Optional[ManifestationInfoDict]
    clip_info: Optional[ClipInfoDict]
    promotion_info: List[PromotionInfoDict]
    supplemental_content_info: List[SupplementalContentInfoDict]
    alternate_content_info: List[AlternateContentInfoDict]
    packaging_info: List[PackagingInfoDict]

    def __init__(self, obj: ExtraObjectMetadataType):
        self.obj = obj

        self.compilation_info = None if obj.compilation_info is None else CompObjectDict(
            entry=[CompObjEntryDict(
                display_name=StringAndLanguageDict(value=entry.display_name.value,
                                                   language=entry.display_name.language),
                entry_number=entry.entry_number,
                entry_class=entry.entry_class,
                content_id=entry.content_id
            ) for entry in obj.compilation_info.entry],
            compilation_class=CompObjClassDict(
                value=obj.compilation_info.compilation_class.value if obj.compilation_info.compilation_class else None,
                has_other_inclusions=obj.compilation_info.compilation_class.has_other_inclusions if obj.compilation_info.compilation_class else None
            )
        )
        self.season_info = None if obj.season_info is None else SeasonInfoDict(
            parent=obj.season_info.parent.value,
            end_date=obj.season_info.end_date,
            season_class=obj.season_info.season_class.copy(),
            number_required=obj.season_info.number_required,
            date_required=obj.season_info.date_required,
            original_title_required=obj.season_info.original_title_required,
            sequence_number=obj.season_info.sequence_number
        )

        self.series_info = None if obj.series_info is None else SeriesInfoDict(
            end_date=obj.series_info.end_date,
            series_class=obj.series_info.series_class,
            number_required=obj.series_info.number_required,
            date_required=obj.series_info.date_required,
            original_title_required=obj.series_info.original_title_required
        )

        self.interactive_material_info = None if obj.interactive_material_info is None else DigitalAssetInteractiveBaseDataDict(
            type_value=obj.interactive_material_info.type_value,
            format_type=obj.interactive_material_info.format_type,
            language=obj.interactive_material_info.language
        )

        self.episode_info = None if obj.episode_info is None else EpisodeInfoDict(
            parent=obj.episode_info.parent.value,
            sequence_info=ContentSequenceInfoDict(
                distribution_number=ComplexSequenceInfoDistributionNumberDict(
                    value=obj.episode_info.sequence_info.distribution_number.value,
                    domain=obj.episode_info.sequence_info.distribution_number.domain
                ) if obj.episode_info.sequence_info.distribution_number else None,
                house_sequence=ComplexSequenceInfoHouseSequenceDict(
                    value=obj.episode_info.sequence_info.house_sequence.value if obj.episode_info.sequence_info.house_sequence else None,
                    domain=obj.episode_info.sequence_info.house_sequence.domain if obj.episode_info.sequence_info.house_sequence else None
                ),
                alternate_number=[ComplexSequenceInfoAlternateNumberDict(
                    value=alt.value,
                    domain=alt.domain
                ) for alt in obj.episode_info.sequence_info.alternate_number]
            ),
            episode_class=obj.episode_info.episode_class.copy(),
            time_slot=obj.episode_info.time_slot
        )

        self.composite_info = [CompositeInfoDict(
            composite_class=comp_info.composite_class,
            element=[CompositeElementDict(
                id=element.id.value if element.id else None,
                other_id=AlternateIdDict(
                    value=element.other_id.value,
                    relation=element.other_id.relation
                ) if element.other_id else None,
                source_start=element.source_start,
                source_duration=element.source_duration,
                components_mode=element.components_mode,
                dest_start=element.dest_start if element.dest_start else None,
                dest_duration=element.dest_duration if element.dest_duration else None,
                description=element.description
            ) for element in comp_info.element]
        ) for comp_info in obj.composite_info]

        self.edit_info = None if obj.edit_info is None else EditInfoDict(
            parent=obj.edit_info.parent.value if obj.edit_info.parent else None,
            edit_use=obj.edit_info.edit_use,
            edit_class=obj.edit_info.edit_class.copy(),
            made_for_region=obj.edit_info.made_for_region.copy(),
            edit_details=[UsageDetailsDict(
                value=detail.value,
                domain=detail.domain
            ) for detail in obj.edit_info.edit_details],
            color_type=obj.edit_info.color_type,
            three_d=obj.edit_info.three_d
        )

        # TODO: this
        # self.manifestation_info = None if obj.manifestation_info is None else ManifestationInfoDict(
        #     parent=obj.manifestation_info.parent.value,
        #     manifestation_class= [] if len(obj.manifestation_info.manifestation_class) >= 0
        #         else [cls for cls in obj.manifestation_info.manifestation_class],
        #     made_for_region= [] if len(obj.manifestation_info.made_for_region) >= 0
        #         else [region for region in obj.manifestation_info.made_for_region],
        #     manifestation_details= [] if len(obj.manifestation_info.manifestation_details) >= 0
        #         else [UsageDetailsDict(
        #             value=detail.value,
        #             domain=detail.domain
        #     ) for detail in obj.manifestation_info.manifestation_details],
        #     digital= None if obj.manifestation_info.digital is None else DigitalTracksDict(
        #         track=[DigitalAssetMetadataDict(
        #             audio=...
        #             video=...
        #             subtitle=...
        #             interactive=...
        #         ) for meta in obj.manifestation_info.digital.track],
        #         container=...
        #     )
        # )

        self.clip_info = None if obj.clip_info is None else ClipInfoDict(
            parent=obj.clip_info.parent.value,
            components_mode=obj.clip_info.components_mode,
            start=obj.clip_info.start,
            duration=[dur for dur in obj.clip_info.duration]
        )

        self.promotion_info = [PromotionInfoDict(
            id=promo.id.value,
            promotion_class=promo.promotion_class
        ) for promo in obj.promotion_info]

        self.supplemental_content_info = [SupplementalContentInfoDict(
            id=supp.id.value,
            supplemental_content_class=supp.supplemental_content_class
        ) for supp in obj.supplemental_content_info]

        self.alternate_content_info = [AlternateContentInfoDict(
            id=alt.id.value,
            alternate_content_class=alt.alternate_content_class
        ) for alt in obj.alternate_content_info]

        self.packaging_info = [PackagingInfoDict(
            id=pack.id.value,
            packaging_class=pack.packaging_class
        ) for pack in obj.packaging_info]

    def __repr__(self):
        dict = self.__dict__.copy()
        del dict["obj"]
        return str(dict)


# Video Service classes below

class ServiceNameDict(TypedDict):
    display_name: str
    sort_name: str
    alternative_name: List[str]
    abbreviation: str
    id_type: str
    organization_id: str


class AlternativeServiceNameDict(TypedDict):
    value: str
    abbreviation: str


class AlternateIDDict(TypedDict):
    value: str
    domain: str


class ServiceDict(TypedDict):
    service_name: ServiceNameDict
    id: str
    alternative_service_name: List[AlternativeServiceNameDict]
    active: bool
    alternate_id: List[AlternateIDDict]
    delivery_model: str
    description: str
    other_affiliation: str
    parent: str
    primary_audio_language: str
    primary_time_zone: str
    region: str


class ServiceMeta:

    def __init__(self, s: Service | ServiceResolutionType):
        self.obj = s
        self.service_name = {
            "display_name": s.service_name.display_name,
            "sort_name": s.service_name.sort_name or "",
            "alternative_name": s.service_name.alternate_name,  # assumed to be a list
            "abbreviation": s.service_name.abbreviation,
            "id_type": s.service_name.id_type,
            "organization_id": s.service_name.organization_id,
        }
        self.id = s.id
        self.alternative_service_name = [
            {"value": n.value, "abbreviation": n.abbreviation} for n in s.alternate_service_name
        ]
        self.active = s.active
        self.alternate_id = [
            {"value": alt.value, "domain": alt.domain} for alt in s.alternate_id
        ]
        self.delivery_model = s.delivery_model
        self.description = s.description
        self.other_affiliation = s.other_affiliation
        self.parent = s.parent
        self.primary_audio_language = s.primary_audio_language
        self.primary_time_zone = s.primary_time_zone
        self.region = s.region

    @classmethod
    def from_string(cls, xml_str):
        return cls(parser.from_string(xml_str, Service, ns))

    def __repr__(self):
        dict = self.__dict__.copy()
        del dict["obj"]
        return str(dict)


class OrgNameDict(TypedDict):
    display_name: Optional[str]  # max_length=256
    sort_name: Optional[str]  # max_length=256
    alternate_name: List[str]  # max_length=256, max_occurs=32
    organization_id: Optional[str]  # No limits specified
    id_type: Optional[StringOrgNameIdType]  # No limits specified


class PhoneDict(TypedDict):
    value: str
    type_value: Optional[str]


class ContactInfoDict(TypedDict):
    name: Optional[str]
    primary_email: Optional[str]
    alternate_email: List[str]
    address: List[str]
    phone: List[PhoneDict]


class PartyMeta:
    def __init__(self, p: Party | PartyResolutionType):
        self.obj = p
        self.id = p.id
        self.party_name = None if p.party_name is None else OrgNameDict(
            display_name=p.party_name.display_name, sort_name=p.party_name.sort_name,
            alternate_name=p.party_name.alternate_name, organization_id=p.party_name.organization_id,
            id_type=p.party_name.id_type
        )
        self.alternate_party_name = p.alternate_party_name.copy()
        self.contact_info = None if p.contact_info is None else ContactInfoDict(
            name=p.contact_info.name,
            primary_email=p.contact_info.primary_email,
            alternate_email=p.contact_info.alternate_email,
            address=p.contact_info.address,
            phone=[PhoneDict(value=phone.value, type_value=phone.type_value) for phone in p.contact_info.phone]
        )
        self.active = p.active
        self.party_account_name = p.party_account_name
        self.allowed_roles = p.allowed_roles.copy()

    @classmethod
    def from_string(cls, xml_str: str):
        return cls(parser.from_string(xml_str, Party, ns))

    def __repr__(self):
        dict = self.__dict__.copy()
        del dict['obj']
        return str(dict)


class FullMeta:
    base_meta: BaseObjectMeta
    extra_meta: ExtraObjectMeta

    @classmethod
    def from_string(cls, xml_str: str):
        return cls(parser.from_string(xml_str, FullObjectInfoType, ns))

    def __init__(self, meta: FullObjectInfoType):
        self.base_meta = BaseObjectMeta(meta.base_object_data)
        self.extra_meta = ExtraObjectMeta(meta.extra_object_metadata)

    def __repr__(self):
        dict = self.__dict__.copy()
        return str(dict)
