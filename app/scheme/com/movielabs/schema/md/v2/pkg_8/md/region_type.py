from dataclasses import dataclass, field
from typing import Optional, Union

from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.string_un_m49 import (
    StringUnM49,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class RegionType:
    class Meta:
        name = "Region-type"

    country: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "pattern": r"[A-Z][A-Z]",
        },
    )
    country_region: Optional[Union[str, StringUnM49]] = field(
        default=None,
        metadata={
            "name": "countryRegion",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "pattern": r"[A-Z][A-Z]-[A-Z0-9]+",
        },
    )
