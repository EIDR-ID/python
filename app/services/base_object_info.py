from typing import List, TypedDict, Optional

from app.scheme.org.eidr.schema.base_object_info_type import BaseObjectInfoType


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

class BaseObjectInfo:
    obj: BaseObjectInfoType = None
    id: str = None
    mode: str = None
    referent_type: str = None
    resource_name: str = None
    alternate_resource_name: List[str] = None
    original_language: List[str] = None
    version_language: List[str] = None
    associated_org: str = None
    release_date: str = None
    country_of_origin: List[str] = None
    status: str = None
    approximate_length: str = None
    alternate_id: List[str] = None
    credits: CreditsDict = None
    registrant_extra: str = None
    description: str = None

    def __init__(self, obj: BaseObjectInfoType):
        self.obj = obj
        self.id = obj.id.value
        self.mode = obj.mode.value
        self.referent_type = obj.referent_type.value
        self.resource_name = obj.resource_name.value
        self.alternate_resource_name = [name.value for name in obj.alternate_resource_name]
        self.original_language = [lang.value for lang in obj.original_language]
        self.version_language = [lang.value for lang in obj.version_language]
        self.associated_org = [ "TYPEDDICT HERE" for org in obj.associated_org]
        self.release_date = obj.release_date.data
        self.country_of_origin = [country.value for country in obj.country_of_origin]
        self.status = obj.status.value
        self.approximate_length = obj.approximate_length.data
        self.alternate_id = [alt.value for alt in obj.alternate_id]
        self.credits = CreditsDict(
            actor=[NameDict(
                display_name=NameAndLanguage(name=name.display_name.value, language=name.display_name.language),
                sort_name=NameAndLanguage(name=name.sort_name.value, language=name.sort_name.language),
                first_given_name=name.first_given_name,
                second_given_name=name.second_given_name,
                family_name=name.family_name,
                suffix=name.suffix,
                moniker=name.moniker
            ) for name in obj.credits.actor],
            director=[NameDict(
                display_name=NameAndLanguage(name=name.display_name.value, language=name.display_name.language),
                sort_name=NameAndLanguage(name=name.sort_name.value, language=name.sort_name.language),
                first_given_name=name.first_given_name,
                second_given_name=name.second_given_name,
                family_name=name.family_name,
                suffix=name.suffix,
                moniker=name.moniker
            ) for name in obj.credits.director]
        )

        self.registrant_extra = obj.registrant_extra
        self.description = obj.description.value