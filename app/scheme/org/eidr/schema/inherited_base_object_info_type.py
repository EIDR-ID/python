from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDate, XmlDuration, XmlPeriod

from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.associated_org_type import (
    AssociatedOrgType,
)
from app.scheme.org.doi.pkg_2010.doischema_avs.creation_structural_type import (
    CreationStructuralType,
)
from app.scheme.org.doi.pkg_2010.doischema_avs.territory_code import TerritoryCode
from    .asset_doitype import AssetDoitype
from    .credits_type import CreditsType
from    .language_type import LanguageType
from    .mode_type import ModeType
from    .referent_type import ReferentType
from    .status_type import StatusType
from    .title_type import TitleType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class InheritedBaseObjectInfoType:
    """ID, Administrators, AlternateIDs, and Description can never be inherited.

    ResourceName and AlternateResourceName are never inherited for
    Seasons or Episodes. Everything else can be, but doesn't have to be.
    """

    class Meta:
        name = "inheritedBaseObjectInfoType"

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
        },
    )
    mode: Optional[ModeType] = field(
        default=None,
        metadata={
            "name": "Mode",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    referent_type: Optional[ReferentType] = field(
        default=None,
        metadata={
            "name": "ReferentType",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    resource_name: Optional[TitleType] = field(
        default=None,
        metadata={
            "name": "ResourceName",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    alternate_resource_name: list[TitleType] = field(
        default_factory=list,
        metadata={
            "name": "AlternateResourceName",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "max_occurs": 128,
        },
    )
    original_language: list[LanguageType] = field(
        default_factory=list,
        metadata={
            "name": "OriginalLanguage",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
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
    associated_org: list[AssociatedOrgType] = field(
        default_factory=list,
        metadata={
            "name": "AssociatedOrg",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "max_occurs": 16,
        },
    )
    release_date: Optional[Union[XmlPeriod, XmlDate]] = field(
        default=None,
        metadata={
            "name": "ReleaseDate",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    country_of_origin: list[TerritoryCode] = field(
        default_factory=list,
        metadata={
            "name": "CountryOfOrigin",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "max_occurs": 32,
        },
    )
    status: Optional[StatusType] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    approximate_length: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ApproximateLength",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    credits: Optional[CreditsType] = field(
        default=None,
        metadata={
            "name": "Credits",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
