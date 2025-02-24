from dataclasses import dataclass, field
from typing import Optional

from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.org_name_type import (
    OrgNameType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class ServiceNameType(OrgNameType):
    class Meta:
        name = "serviceNameType"

    abbreviation: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
