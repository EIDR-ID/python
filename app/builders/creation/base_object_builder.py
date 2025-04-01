from enum import Enum
from typing import Union, Optional

from xsdata.models.datatype import XmlDate, XmlPeriod, XmlDuration

from app.scheme.org.doi.pkg_2010.doischema_avs import CreationStructuralType
from app.scheme.org.doi.pkg_2010.doischema_avs.territory_code import TerritoryCode
from app.scheme.org.eidr.schema import AlternateIdrelationType, CreateType, CreationType
from app.scheme.org.eidr.schema.referent_type import ReferentType
from app.scheme.org.eidr.schema.creation_full_info import CreationFullInfo
from app.scheme.org.eidr.schema.mode_type import ModeType
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
from app.scheme.com.movielabs.schema.md.v2.pkg_8.md.string_org_name_id_type import StringOrgNameIdType
from app.scheme.com.movielabs.schema.md.v2.pkg_8.md.string_associated_org_role import StringAssociatedOrgRole
from app.scheme.com.movielabs.schema.md.v2.pkg_8.md.string_and_language_type import StringAndLanguageType
from app.scheme.com.movielabs.schema.md.v2.pkg_8.md.person_name_type import PersonNameType
from app.scheme.com.movielabs.schema.md.v2.pkg_8.md.associated_org_type import AssociatedOrgType
from .helpers import get_enum

class BaseObjectBuilder:
    """
    This class is utilized to build the base object data element of type CreationFullInfo or SelfDefinedInfo for any
    type of record i.e. Season, Series, Episode etc.

    Attributes:
        creation_type(CreationType): The creation type of the record being built
        structural_type (Optional[CreationStructuralType]): The structural type of the record.
        mode (Optional[ModeType]): The mode type of the record.
        referent_type (Optional[ReferentType]): The referent type of the record.
        resource_name (Optional[TitleType]): The name of the resource.
        alternate_resource_name (list[TitleType]): A list of alternate resource names.
        original_language (list[LanguageType]): A list of original languages.
        version_language (list[LanguageType]): A list of version languages.
        associated_org (list[AssociatedOrgType]): A list of associated organizations.
        release_date (Optional[Union[XmlPeriod, XmlDate]]): The release date of the record.
        country_of_origin (list[TerritoryCode]): A list of countries of origin.
        status (Optional[StatusType]): The status of the record.
        approximate_length (Optional[XmlDuration]): The approximate length of the record.
        alternate_id (list[AlternateIdtype]): A list of alternate IDs.
        administrators (Optional[AdministratorsInfoType]): The administrators of the record.
        directors (Optional[StringAndLanguageType]): The directors of the record.
        actors (Optional[StringAndLanguageType]): The actors of the record.
        registrant_extra (Optional[str]): Extra information provided from the registrant.
        description (Optional[DescriptionType]): The description of the record.
    """
    def __init__(self, creation_type: CreationType):
        self.creation_type = creation_type
        self.structural_type: Optional[CreationStructuralType] = CreationStructuralType.ABSTRACTION
        self.mode: Optional[ModeType] = None
        self.referent_type: Optional[ReferentType] = None
        self.resource_name: Optional[TitleType] = None
        self.alternate_resource_name: list[TitleType] = []
        self.original_language: list[LanguageType] = []
        self.version_language: list[LanguageType] = []
        self.associated_org: list[AssociatedOrgType] = []
        self.release_date: Optional[Union[XmlPeriod, XmlDate]] = None
        self.country_of_origin: list[TerritoryCode] = []
        self.status: Optional[StatusType] = None
        self.approximate_length: Optional[XmlDuration] = None
        self.alternate_id: list[AlternateIdtype] = []
        self.administrators: Optional[AdministratorsInfoType] = None
        self.directors: Optional[list[PersonNameType]] = []
        self.actors: Optional[list[PersonNameType]] = []
        self.registrant_extra: Optional[str] = None
        self.description: Optional[DescriptionType] = None

    def build_creation_full_info(self) -> CreationFullInfo:
        return CreationFullInfo(
            structural_type=self.structural_type,
            mode=self.mode,
            referent_type=self.referent_type,
            resource_name=self.resource_name,
            alternate_resource_name=self.alternate_resource_name,
            original_language=self.original_language,
            version_language=self.version_language,
            release_date=self.release_date,
            country_of_origin=self.country_of_origin,
            status=self.status,
            approximate_length=self.approximate_length,
            alternate_id=self.alternate_id,
            administrators=self.administrators,
            credits = CreditsType(
                director=self.directors,
                actor=self.actors,
            ),
            registrant_extra=self.registrant_extra,
            description=self.description,
        )

    def set_creation_type(self, creation_type: Union[CreationType,str]):
        """
        Set the creation_type of the record object being built
        :param creation_type: the creation type of the record
        :return: none
        """
        self.creation_type = creation_type

    # TODO: finalize documentation and validation
    def set_structural_type(self, structural_type: Union[CreationStructuralType, str]):
        """
        Set the structural type of the record. Most records default to the structural type:
        "Abstraction" except Manifestations, Clips, Edits and Compilations

        - "Abstraction"
        - "Digital"
        - "Performance"
        - "Physical"
        - "Restricted"
        :param structural_type: the structural type of the record.
        """
        try:
            self.structural_type = get_enum(CreationStructuralType, structural_type)
        except ValueError as e:
            raise e
        return self

    def set_mode_type(self, mode_type: Union[ModeType, str]):
        """
        Set the mode type of the record. If AudioVisual then Release Date field must
        bet after 1893. If Visual then the 'mode' of either Original Language or Version
        Language fields be not be Audio.

        - "Audio"
        - "Visual"
        - "AudioVisual"
        - "Other"
        This field is **required**
        :param mode_type: the mode type of the record.
        """
        try:
            self.mode = get_enum(ModeType, mode_type)
        except ValueError as e:
            raise e
        return self

    def set_referent_type(self, referent_type: Union[ReferentType,str]):
        """
        Set the referent type of the record. Referent type typically matches
        the type of record built i.e a series record's referent_type is Series.
        Basic, Episode, and Composite records are fixed to either TV, Movie, Short ,
        Web or Supplemental. Manifestation, Edit, and Clip records can inherit this field
        or if set must be either TV, Movie, Short, Web, or Supplemental.

        - "Series"
        - "Podcast"
        - "TV"
        - "Movie"
        - "Short"
        - "Web"
        - "Compilation"
        - "Interactive Material"
        - "Supplemental"
        :param referent_type:
        """
        try:
            self.referent_type = get_enum(ReferentType, referent_type)
        except ValueError as e:
            raise e
        return self

    def set_resource_name(self,
                          value: str,
                          lang: str,
                          title_class: Optional[Union[TitleClassType, str]] = None,
                          system_generated: Optional[bool] = None):
        """
        The primary name of the work. This field is **conditionally required**: Certain derived types
        can use a system-generated or inherited title which can be supplied by the registry.
        :param value: name of the resource
        :param lang: language of the resource
        :param title_class: the title class of the record:
            "release","abbreviated","working","acronym","fan-based" "internal","series numeric",
            "series date","regional" "broadcast","AKA", "FKA", "transliterated", "other"
        :param system_generated: boolean that defines whether this resource is system generated
        """
        self.resource_name = TitleType(
            value=value,
            title_class=get_enum(TitleClassType, title_class) if title_class is not None else None,
            lang=lang,
            system_generated=system_generated if system_generated is not None else None,
        )
        return self

    def add_alternate_resource_name(
            self,
            value: str,
            lang: str,
            title_class: Optional[Union[TitleType, str]] = None,
            system_generated: Optional[bool] = None
    ):
        """
        Add alternate names for the record. This is an optional field when creating any record
        :param value: the alternate name of the record | Required
        :param lang: language of the alternate name (not the lang of the record) | Required
        :param title_class general type of resource name | Optional
        :param system_generated: identify whether this resource is system generated | Optional
        """
        self.alternate_resource_name.append(
            TitleType(
                value=value,
                title_class=get_enum(TitleClassType, title_class) if title_class is not None else None,
                lang=lang,
                system_generated=system_generated if system_generated is not None else None,
            )
        )
        return self

    def set_release_date(self, release_date: Union[XmlDate, XmlPeriod, str]):
        """
        Set the release date of the record
        :param release_date: this can be of the following formats: "YYYY-MM-DD", "YYYY-MM", "YYYY"
        """
        if isinstance(release_date, str):
            # TODO: figure out a way to decide from a string if it's either a valid XmlDate or XmlPeriod
            self.release_date = XmlDate.from_string(release_date)
            pass
        elif isinstance(release_date, XmlDate):
            self.release_date = release_date
        elif isinstance(release_date, XmlPeriod):
            self.release_date = release_date
        else:
            raise TypeError(f"Expected either a string, XmlDate, or XmlPeriod, but got {type(release_date)}")
        return self

    def set_status(self, status: Union[StatusType, str]):
        """
        Set the status of the record:
        - "valid",
        - "in development",
        - "alias"
        :param status: the status of the record
        """
        self.status = get_enum(StatusType, status)
        return self

    def set_approximate_length(self, approx_length: Union[XmlDuration, str]):
        """
        :param approx_length: the approximate length of the record
        """
        if isinstance(approx_length, str):
            self.approximate_length = XmlDuration(approx_length)
        elif isinstance(approx_length, XmlDuration):
            self.approximate_length = approx_length
        else:
            raise TypeError(f"Expected either a string or XmlDuration, but got {type(approx_length)}")
        return self

    def set_administrators(self, registrant: str, metadata_authority: Optional[list[str]] = None):
        """
        Set the administrators of this record
        :param registrant:
        :param metadata_authority:
        """
        if isinstance(registrant, str) and (isinstance(metadata_authority, list) or metadata_authority is None):
            self.administrators = AdministratorsInfoType(
                registrant=RegistrantType(value=registrant),
                metadata_authority=[
                    MetadataAuthorityType(value=registrant) for registrant in metadata_authority
                ] if metadata_authority is not None else None,
            )
        else:
            raise TypeError(
                f"Expected a string for registrant and a list of strings for metadata_authority, "
                f"but got {type(registrant)} and {type(metadata_authority)}"
            )
        return self

    def add_original_language(
            self,
            value: str,
            mode: Union[ModeType, str],
            language_track_type: Optional[Union[LanguageTrackTypeType, str]] = None
    ):
        """
        Add an original language element of type (Language Type) to the record
        :param value the original language
        :param mode Audio or Visual
        :param language_track_type: "commentary", "dialogcentric", "narration", "primary", "silent", "silent-omitted
        "other", "easyreader", "forced", "large", "noforced", "normal", "SDH", and "singalong"
        """

        self.original_language.append(
            LanguageType(
                value=value,
                mode=get_enum(DoiModeRestricted, mode),
                type_value=get_enum(
                    LanguageTrackTypeType, language_track_type
                ) if language_track_type is not None else None
            )
        )
        return self

    def add_version_language(
            self,
            value: str,
            mode: str,
            language_track_type: Optional[Union[LanguageTrackTypeType, str]] = None
    ):
        """
        Language of derivative object to the extent they differ from the langs defined in the
        original language field. Only Manifestation, Edit and Clip need this field other
        records must have this field "absent"
        :param value the original language
        :param mode Audio or Visual
        :param language_track_type: "commentary", "dialogcentric", "narration", "primary", "silent", "silent-omitted
        "other", "easyreader", "forced", "large", "noforced", "normal", "SDH", and "singalong"
        """
        self.version_language.append(LanguageType(
            value=value,
            mode=get_enum(DoiModeRestricted, mode) if mode is not None else None,
            type_value=get_enum(
                LanguageTrackTypeType, language_track_type
            ) if language_track_type is not None else None
        ))
        return self

    def set_country_of_origin(self, country_of_origin: list[Union[TerritoryCode, str]]):
        """
        Set the home countries of the companies that had primary control of the creation of this work.
        This field is **conditionally required**: may be inherited in child records.
        :param country_of_origin: list of country codes
        """
        self.country_of_origin.extend([get_enum(TerritoryCode, code) for code in country_of_origin])
        return self

    def add_country_of_origin(self, country_of_origin: Union[TerritoryCode, str]):
        """
        Add home countries of the companies that had primary control of the creation of this work.
        This field is **conditionally required**: may be inherited in child records.
        """
        pass

    def add_director(self,display_name: str, lang:str):
        """
        Add a director to the credits. **Max of 2 directors per record**
        :param display_name: the display name
        :param lang: langauge of the display name
        """
        if isinstance(display_name, str) and isinstance(lang, str):
            self.directors.append(
                PersonNameType(
                    display_name=StringAndLanguageType(
                        value=display_name,
                        language=lang,
                    )
                )
            )
        else:
            raise TypeError(f"Expected a string for 'display_name', but got {type(display_name)} "
                            f"and string for 'lang'{type(lang)}")
        return self

    def add_actor(self,display_name: StringAndLanguageType, lang:str):
        """
        Add an actor to the credits. **Max of 4 actors per record**.
        :param display_name: the display name
        :param lang: langauge of the display name
        """
        if isinstance(display_name, str) and isinstance(lang, str):
            self.actors.append(
                PersonNameType(
                    display_name=StringAndLanguageType(
                        value=display_name,
                        language=lang
                    ),
                )
            )
        else:
            raise TypeError(f"Expected a string for 'display_name', but got {type(display_name)} "
                            f"and string for 'lang'{type(lang)}")
        return self

    def add_associated_org(
            self,
            display_name: str,
            role: Union[StringAssociatedOrgRole, str],
            sort_name: Optional[str],
            alternate_name: Optional[list[str]],
            organization_id: Optional[str],
            id_type: Optional[Union[StringOrgNameIdType, str]] = None
    ):
        """
        Add an organization responsible for creating the work. This field is **conditionally required**:
        Required if at least 1 Director or 4 actors are **not** present in the credits field.
        :param display_name: the display name of the organization
        :param role: contribution of the AssociatedOrg to the work i.e. producer, editor etc.
        :param sort_name:
        :param alternate_name: additional names for the organization
        :param organization_id: unique identifier of the organization
        :param id_type: type of id used in the organization_id field
        """
        try:
            self.associated_org.append(
                AssociatedOrgType(
                    display_name=display_name,
                    role=role,
                    sort_name=sort_name,
                    alternate_name=alternate_name,
                    organization_id=organization_id,
                    id_type=id_type
                )
            )
        except TypeError as e:
            raise e
        return self

    #TODO: This field doesn't have the necessary fields in the corresponding data class, so create them
    def add_alternate_id(self, value: str, relation: Union[AlternateIdrelationType, str]):
        """
        Add a non-EIDR identifier(alternate id) to the record
        :param value: the alternate id **Required**
        :param relation: relation type of the alt id
        """
        if isinstance(value, str):
            self.alternate_id.append(
                AlternateIdtype(
                    value=value,
                    relation=get_enum(AlternateIdrelationType, relation)
                )
            )
        else:
            raise TypeError(f"Expected a string for 'value', but got {type(value)}")
        return self

    def set_registrant_extra(self, registrant_extra: str):
        """
        Additional information provided by the registrant. This field is **optional**.
        :param registrant_extra: the extra information provided by the registrant
        :return: Type[BaseObjectDataBuilder]
        """
        self.registrant_extra = registrant_extra
        return self

    def set_description(self, value: str, lang: str):
        """
        Additional information regarding the nature of the work to assist discovery and manual de-duplication.
        This field is **optional**.
        :param value: the description of this work **Required**
        :param lang: the language of the description e.g. en,fr,etc. **Required**
        :return:
        """
        if isinstance(value, str) and isinstance(lang, str):
            self.description = DescriptionType(
                value=value,
                lang=lang
            )
        else:
            raise TypeError(f"Expected a string for 'value' but got {type(value)} "
                            f"and string for 'lang' but got {type(lang)}")
        return self

    # TODO: implement remaining extraobjectmeta builer classes:digitalassetinteracive, seasoninfotype, episodeinfotype,
    # editinfotype episodeinfotype, editinfotype, manifestationtype, clipinfotype, combobjtype, compositeinfotype


