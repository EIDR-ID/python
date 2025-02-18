from dataclasses import dataclass, field
from typing import Optional

from scheme.org.eidr.schema.alternate_idtype import AlternateIdtype
from scheme.org.eidr.schema.asset_doitype import AssetDoitype

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class AlternateIdsType:
    """
    An asset's AlternateIDs only.
    """

    class Meta:
        name = "alternateIDsType"

    id: Optional[AssetDoitype] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
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
