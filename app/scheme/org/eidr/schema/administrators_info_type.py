from dataclasses import dataclass, field
from typing import Optional

from    .metadata_authority_type import (
    MetadataAuthorityType,
)
from    .registrant_type import RegistrantType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class AdministratorsInfoType:
    """
    Used in provenanceInfoType, baseObjectInfoType, and
    selfDefinedBaseObjectInfoType.
    """

    class Meta:
        name = "administratorsInfoType"

    registrant: Optional[RegistrantType] = field(
        default=None,
        metadata={
            "name": "Registrant",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    metadata_authority: list[MetadataAuthorityType] = field(
        default_factory=list,
        metadata={
            "name": "MetadataAuthority",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "max_occurs": 4,
        },
    )
