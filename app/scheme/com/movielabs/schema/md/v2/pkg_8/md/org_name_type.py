from dataclasses import dataclass, field
from typing import Optional

from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.string_org_name_id_type import (
    StringOrgNameIdType,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class OrgNameType:
    """
    Restrict cardinalities, enumerate values for idType attribute.
    """

    class Meta:
        name = "OrgName-type"

    display_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "DisplayName",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "max_length": 256,
        },
    )
    sort_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SortName",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "max_length": 256,
        },
    )
    alternate_name: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AlternateName",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "max_occurs": 32,
            "max_length": 256,
        },
    )
    organization_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "organizationID",
            "type": "Attribute",
        },
    )
    id_type: Optional[StringOrgNameIdType] = field(
        default=None,
        metadata={
            "name": "idType",
            "type": "Attribute",
        },
    )
