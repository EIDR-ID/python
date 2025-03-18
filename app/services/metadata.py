from typing import List, TypedDict, Optional

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig

config = ParserConfig()
context = XmlContext()
parser = XmlParser(context=context, config=config)
ns = {"": "http://www.eidr.org/schema"}

from app.scheme.org.eidr.schema import FullObjectInfoType
from app.scheme.org.eidr.schema.base_object_info_type import BaseObjectInfoType, AssociatedOrgType, CreationStructuralType, ModeType, ReferentType, StatusType, TitleType


class NameAndLanguage(TypedDict):
    name: str
    language: str


class NameDict(TypedDict):
    display_name: NameAndLanguage
    sort_name: NameAndLanguage
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




class BaseObjectMeta:
    obj: BaseObjectInfoType | None = None
    structural_type: str = None # Mandatory
    mode: str = None # Mandatory
    referent_type: str = None # Mandatory
    resource_name: str = None # Mandatory
    administrators: AdministratorsDict = None
    alternate_resource_name: List[str] | None = None
    original_language: List[str] = None
    version_language: List[str] = None
    associated_org: List[str] = None
    release_date: str = None # Mandatory
    country_of_origin: List[str] = None
    status: str | None = None
    approximate_length: str | None = None
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
        self.structural_type = obj.structural_type.value
        self.mode = obj.mode.value
        self.referent_type = obj.referent_type.value
        self.resource_name = obj.resource_name.value
        self.administrators = AdministratorsDict(
            registrant=obj.administrators.registrant.value,
            metadata_authority=[auth.value for auth in obj.administrators.metadata_authority]
        )
        self.alternate_resource_name = [name.value for name in obj.alternate_resource_name]
        self.original_language = [lang.value for lang in obj.original_language]
        self.version_language = [lang.value for lang in obj.version_language]
        self.associated_org = [org.role.name for org in obj.associated_org]
        self.release_date = obj.release_date.data
        self.country_of_origin = [country.value for country in obj.country_of_origin]
        self.status = obj.status.value
        self.approximate_length = obj.approximate_length.data
        self.alternate_id = [alt.value for alt in obj.alternate_id]
        self.credits = CreditsDict(
            actor=[NameDict(
                display_name=NameAndLanguage(name=name.display_name.value or None, language=name.display_name.language or None),
                sort_name=NameAndLanguage(name=name.sort_name.value, language=name.sort_name.language) if name.sort_name else None,
                first_given_name=name.first_given_name or None,
                second_given_name=name.second_given_name or None,
                family_name=name.family_name or None,
                suffix=name.suffix or None,
                moniker=name.moniker or None
            ) for name in obj.credits.actor],
            director=[NameDict(
                display_name=NameAndLanguage(name=name.display_name.value or None, language=name.display_name.language or None),
                sort_name=NameAndLanguage(name=name.sort_name.value or None, language=name.sort_name.language or None),
                first_given_name=name.first_given_name or None,
                second_given_name=name.second_given_name or None,
                family_name=name.family_name or None,
                suffix=name.suffix or None,
                moniker=name.moniker or None
            ) for name in obj.credits.director]
        )

        self.registrant_extra = obj.registrant_extra
        self.description = obj.description.value

class ExtraObjectMeta:
    ...

class FullMeta:
    base_meta: BaseObjectMeta
    extra_meta: ExtraObjectMeta

    @classmethod
    def from_string(cls, res_str: str):
        return cls(parser.from_string(res_str, FullObjectInfoType, ns))

    def __init__(self, meta: FullObjectInfoType):
        self.base_meta = BaseObjectMeta(meta.base_object_data)
        self.extra_meta = ExtraObjectMeta()
