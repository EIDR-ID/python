from dataclasses import dataclass, field
from typing import Optional

from scheme.org.eidr.schema.asset_doitype import AssetDoitype
from scheme.org.eidr.schema.linked_alternate_idtype import (
    LinkedAlternateIdtype,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class LinkedAlternateIdsType:
    """
    An asset's AlternateIDs and associated URLs.
    """

    class Meta:
        name = "linkedAlternateIDsType"

    id: Optional[AssetDoitype] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    linked_alternate_id: list[LinkedAlternateIdtype] = field(
        default_factory=list,
        metadata={
            "name": "LinkedAlternateID",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
