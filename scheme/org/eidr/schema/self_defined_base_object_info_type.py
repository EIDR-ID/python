from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDate, XmlDuration, XmlPeriod

from scheme.com.movielabs.schema.md.v2.pkg_8.md.associated_org_type import (
    AssociatedOrgType,
)
from scheme.org.doi.pkg_2010.doischema_avs.creation_structural_type import (
    CreationStructuralType,
)
from scheme.org.doi.pkg_2010.doischema_avs.territory_code import TerritoryCode
from scheme.org.eidr.schema.administrators_info_type import (
    AdministratorsInfoType,
)
from scheme.org.eidr.schema.alternate_idtype import AlternateIdtype
from scheme.org.eidr.schema.asset_doitype import AssetDoitype
from scheme.org.eidr.schema.credits_type import CreditsType
from scheme.org.eidr.schema.description_type import DescriptionType
from scheme.org.eidr.schema.language_type import LanguageType
from scheme.org.eidr.schema.mode_type import ModeType
from scheme.org.eidr.schema.referent_type import ReferentType
from scheme.org.eidr.schema.status_type import StatusType
from scheme.org.eidr.schema.title_type import TitleType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class SelfDefinedBaseObjectInfoType:
    """This is what you get when you do a resolution for self-defined metadata.

    ID and Administrators must be defined on every object. AlternateIDs,
    RegistrantExtra are never inherited, but can be optionally provided.
    Everything else can come from self or parent, and hence is optional
    here. VersionLanguages are only those defined on the object, rather
    than constructed from a Manifestation
    """

    class Meta:
        name = "selfDefinedBaseObjectInfoType"

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
    alternate_id: list[AlternateIdtype] = field(
        default_factory=list,
        metadata={
            "name": "AlternateID",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    administrators: Optional[AdministratorsInfoType] = field(
        default=None,
        metadata={
            "name": "Administrators",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
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
    registrant_extra: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegistrantExtra",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "max_length": 128,
        },
    )
    description: Optional[DescriptionType] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
