from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDate, XmlPeriod

from scheme.org.doi.pkg_2010.doischema_avs.creation_structural_type import (
    CreationStructuralType,
)
from scheme.org.eidr.schema.asset_doitype import AssetDoitype
from scheme.org.eidr.schema.language_type import LanguageType
from scheme.org.eidr.schema.referent_type import ReferentType
from scheme.org.eidr.schema.relationship_info_type import RelationshipInfoType
from scheme.org.eidr.schema.status_type import StatusType
from scheme.org.eidr.schema.title_type import TitleType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class SimpleInfoType:
    class Meta:
        name = "simpleInfoType"

    id: Optional[AssetDoitype] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    structural_type: Optional[CreationStructuralType] = field(
        default=None,
        metadata={
            "name": "StructuralType",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    referent_type: Optional[ReferentType] = field(
        default=None,
        metadata={
            "name": "ReferentType",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    resource_name: Optional[TitleType] = field(
        default=None,
        metadata={
            "name": "ResourceName",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    original_language: list[LanguageType] = field(
        default_factory=list,
        metadata={
            "name": "OriginalLanguage",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "min_occurs": 1,
            "max_occurs": 32,
        },
    )
    version_language: list[LanguageType] = field(
        default_factory=list,
        metadata={
            "name": "VersionLanguage",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "max_occurs": 64,
        },
    )
    release_date: Optional[Union[XmlPeriod, XmlDate]] = field(
        default=None,
        metadata={
            "name": "ReleaseDate",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    status: Optional[StatusType] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    relationship: list[RelationshipInfoType] = field(
        default_factory=list,
        metadata={
            "name": "Relationship",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
