from typing import Union, Optional

from xsdata.models.datatype import XmlDate, XmlPeriod, XmlDuration, XmlDateTime

from app.scheme.com.movielabs.schema.md.v2.pkg_8.md import AssociatedOrgType, PersonNameType, StringAndLanguageType
from app.scheme.org.doi.pkg_2010.doischema_avs import CreationStructuralType, TerritoryCode
from app.scheme.org.eidr.schema.referent_type import ReferentType
from app.scheme.org.eidr.schema.creation_full_info import CreationFullInfo
from app.scheme.org.eidr.schema.mode_type import ModeType
from app.scheme.org.eidr.schema.creation_self_defined_info import CreationSelfDefinedInfo
from app.scheme.org.eidr.schema.title_type import TitleType
from app.scheme.org.eidr.schema.status_type import StatusType
from app.scheme.org.eidr.schema.alternate_idtype import AlternateIdtype
from app.scheme.org.eidr.schema.administrators_info_type import AdministratorsInfoType
from app.scheme.org.eidr.schema.credits_type import CreditsType
from app.scheme.org.eidr.schema.description_type import DescriptionType
from app.scheme.org.eidr.schema.title_class_type import TitleClassType
from app.scheme.org.eidr.schema.doi_mode_restricted import DoiModeRestricted
from app.scheme.org.eidr.schema.language_track_type_type import LanguageTrackTypeType
from app.scheme.org.eidr.schema.language_type import LanguageType
from app.scheme.org.eidr.schema.registrant_type import RegistrantType
from app.scheme.org.eidr.schema.metadata_authority_type import MetadataAuthorityType
from app.scheme.org.eidr.schema.series_info_type import SeriesInfoType
from app.scheme.org.eidr.schema.series_class_type import SeriesClassType


def get_enum(enum_class, value: str):
    """
    Helper function to get the corresponding enum given a string value and its class
    """
    enum_values = [type.value for type in enum_class]
    if value not in enum_values:
        raise ValueError("'value' is invalid, must be one of the following: {}".format(enum_values))
    return enum_class(value)

class BaseObjectDataBuilder:
    """
    This class is utilized to build the base object data element of type (CreationFullInfo or SelfDefinedInfo)
    """
    structural_type: Optional[CreationStructuralType] = None
    mode: Optional[ModeType] = None
    referent_type: Optional[ReferentType] = None
    resource_name: Optional[TitleType] = None
    alternate_resource_name: list[TitleType]
    original_language: list[LanguageType] = []
    version_language: list[LanguageType] = []
    associated_org: list[AssociatedOrgType] = []
    release_date: Optional[Union[XmlPeriod, XmlDate]] = None
    country_of_origin: list[TerritoryCode] = []
    status: Optional[StatusType] = None
    approximate_length: Optional[XmlDuration] = None
    alternate_id: list[AlternateIdtype] = []
    administrators: Optional[AdministratorsInfoType] = None
    credits: Optional[CreditsType] = None
    registrant_extra: Optional[str] = None
    description: Optional[DescriptionType] = None

    @classmethod
    def build_creation_full_info(cls) -> CreationFullInfo:
        return CreationFullInfo(
            structural_type=cls.structural_type,
            mode=cls.mode,
            referent_type=cls.referent_type,
            resource_name=cls.resource_name,
            alternate_resource_name=cls.alternate_resource_name,
            original_language=cls.original_language,
            version_language=cls.version_language,
            release_date=cls.release_date,
            country_of_origin=cls.country_of_origin,
            status=cls.status,
            approximate_length=cls.approximate_length,
            alternate_id=cls.alternate_id,
            administrators=cls.administrators,
            credits=cls.credits,
            registrant_extra=cls.registrant_extra,
            description=cls.description,
        )

    @classmethod
    def build_self_defined_info(cls) -> CreationSelfDefinedInfo:
        return CreationSelfDefinedInfo(
            structural_type=cls.structural_type,
            mode=cls.mode,
            referent_type=cls.referent_type,
            resource_name=cls.resource_name,
            alternate_resource_name=cls.alternate_resource_name,
            original_language=cls.original_language,
            version_language=cls.version_language,
            release_date=cls.release_date,
            country_of_origin=cls.country_of_origin,
            status=cls.status,
            approximate_length=cls.approximate_length,
            alternate_id=cls.alternate_id,
            administrators=cls.administrators,
            credits=cls.credits,
            registrant_extra=cls.registrant_extra,
            description=cls.description,
        )

    # TODO: finalize documentation and validation
    @classmethod
    def set_structural_type(cls, structural_type: str):
        """
        - "Abstraction"
        - "Digital"
        - "Performance"
        - "Physical"
        - "Restricted"
        :param structural_type: str
        """
        cls.structural_type  = get_enum(CreationStructuralType, structural_type)
        return cls

    @classmethod
    def set_mode_type(cls, mode_type: str):
        """
        - "Audio"
        - "Visual"
        - "AudioVisual"
        - "Other"
        :param mode_type: str
        """
        cls.mode = get_enum(ModeType, mode_type)
        return cls

    @classmethod
    def set_referent_type(cls, referent_type: str):
        """
        - "Series"
        - "Podcast"
        - "Season"
        - "TV"
        - "Movie"
        - "Short"
        - "Web"
        - "Compilation"
        - "Interactive Material"
        - "Supplemental"
        :param referent_type: str
        """
        cls.referent_type = ReferentType(referent_type)
        return cls

    @classmethod
    def set_resource_name(cls,
                          value: str,
                          lang:str,
                          title_class: Optional[str] = None,
                          system_generated: Optional[bool] = None):
        """
        Set the resource name of this record
        :param value: name of this resource
        :param lang: language of this resource
        :param title_class: following options: "release", "abbreviated", "working", "acronym", "fan-based"
        "internal", "series numeric","series date", "regional"
        "broadcast", "AKA", "FKA", "transliterated", and "other"
        :param system_generated: bool whether this resource is system generated
        """
        cls.resource_name = TitleType(
            value=value,
            title_class= get_enum(TitleClassType,title_class) if title_class is not None else None,
            lang=lang,
            system_generated=system_generated if system_generated is not None else None,
        )
        return cls

    @classmethod
    def set_release_date(cls,release_date: str):
        """
        Set the release date of the record
        :param release_date: this can be of the following formats: "YYYY-MM-DD", "YYYY-MM", "YYYY"
        """
        # using the XmlDate type for now, XmlPeriod is also an option
        cls.release_date = XmlDate.from_string(release_date)
        return cls

    @classmethod
    def set_status(cls, status: str):
        """
        Options:
        "valid",
        "in development",
         and "alias"
        :param status: the status of the record
        """
        cls.status = get_enum(StatusType, status)
        return cls

    @classmethod
    def set_approximate_length(cls,approx_length: str):
        """
        Set the approximate length of the record
        :param approx_length: the approximate length of the record
        """
        try:
            cls.approximate_length = XmlDuration(approx_length)
        except ValueError as e:
            raise ValueError(f"Error occurred trying to set the approximate length: {e}")
        return cls

    @classmethod
    def set_administrators(cls,registrant: str, metadata_authority:Optional[list[str]] = None):
        """
        Set the administrators of this record
        :param registrant:
        :type registrant: str
        :param metadata_authority:
        :type metadata_authority: list[str]
        """
        cls.administrators = AdministratorsInfoType(
            registrant= RegistrantType(value=registrant),
            metadata_authority= [MetadataAuthorityType(value=registrant) for registrant in metadata_authority] if metadata_authority else None,
        )
        return cls

    @classmethod
    def add_original_language(cls, value: str, mode: str, language_track_type: Optional[str]):
        """
        Add an original language element of type (Language Type) to the record
        :param value the original language
        :param mode Audio or Visual
        :param language_track_type: "commentary", "dialogcentric", "narration", "primary", "silent", "silent-omitted
        "other", "easyreader", "forced", "large", "noforced", "normal", "SDH", and "singalong"
        """
        cls.original_language.append(LanguageType(
            value=value,
            mode= get_enum(DoiModeRestricted, mode) if mode is not None else None,
            type_value = LanguageTrackTypeType(language_track_type) if language_track_type else None
        ))
        return cls

    @classmethod
    def add_version_language(cls, value:str, mode:str, language_track_type:Optional[str]):
        """
        Add a version language element of type (Language Type) to the record
        :param value the original language
        :param mode Audio or Visual
        :param language_track_type: "commentary", "dialogcentric", "narration", "primary", "silent", "silent-omitted
        "other", "easyreader", "forced", "large", "noforced", "normal", "SDH", and "singalong"
        """
        cls.version_language.append(LanguageType(
            value=value,
            mode= get_enum(DoiModeRestricted, mode) if mode is not None else None,
            type_value = LanguageTrackTypeType(language_track_type) if language_track_type else None
        ))
        return cls

    @classmethod
    def set_country_of_origin(cls,country_of_origin: list[str]):
        """
        Set the country of origin for this record
        :param country_of_origin: the country of origin -> Territory Code
        """
        cls.country_of_origin = [TerritoryCode(code) for code in country_of_origin]
        return cls

    #TODO: finish implementation, just allows a single director to be set
    @classmethod
    def set_credits(cls,director_name, director_name_language):
        """
        Set the credits for this record which includes:
        """
        cls.credits = CreditsType(
            director= [PersonNameType(
                display_name= StringAndLanguageType(
                    value=director_name,
                    language=director_name_language
                )
            )],
        )
        return cls

        # TODO: implement remaining setters: alt_resource, associated_org, alternate_id, registrant_extra, description

    #TODO: implement remaining extraobjectmeta builer classes:digitalassetinteracive, seasoninfotype, episodeinfotype,
    # editinfotype episodeinfotype, editinfotype, manifestationtype, clipinfotype, combobjtype, compositeinfotype
class SeriesInfoBuilder:
    """
    Extra Object MetaData factory for a Series record
    """
    end_date: Optional[Union[XmlDate, XmlDateTime]] = None
    number_required: Optional[bool] = None
    date_required: Optional[bool] = None
    original_title_required: Optional[bool] = None
    series_class: Optional[SeriesClassType] = None

    @classmethod
    def build(cls) -> SeriesInfoType:
        return SeriesInfoType(
            end_date=cls.end_date,
            series_class=cls.series_class,
            number_required=cls.number_required,
            date_required=cls.date_required,
            original_title_required=cls.original_title_required,
        )
    @classmethod
    def set_end_date(cls, end_date: str):
        """
        set the end date of the record
        :param end_date the end date of the record Format "YYYY-MM-DD"
        """
        cls.end_date = XmlDate.from_string(end_date)
        return cls

    @classmethod
    def set_series_class(cls, series_class:str):
        """
        Set the series class of the record
        :param series_class: the series class of the record
        """
        cls.series_class = get_enum(
            enum_class=SeriesClassType,
            value=series_class
        ) if series_class is not None else None
        return cls

    @classmethod
    def set_number_required(cls, number_required: bool):
        """
        Set the number required field
        :param number_required: bool
        """
        cls.number_required = number_required
        return cls

    @classmethod
    def set_date_required(cls, date_required: bool):
        """
        Set the date required field
        """
        cls.date_required = date_required
        return cls

    @classmethod
    def set_original_title_required(cls, original_title_required: bool):
        """
        Set the original title required field
        """
        cls.original_title_required = original_title_required
        return cls
