from dataclasses import dataclass, field
from typing import Optional

from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.org_name_type import (
    OrgNameType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.string_associated_org_role import (
    StringAssociatedOrgRole,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class AssociatedOrgType(OrgNameType):
    class Meta:
        name = "AssociatedOrg-type"

    role: Optional[StringAssociatedOrgRole] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
