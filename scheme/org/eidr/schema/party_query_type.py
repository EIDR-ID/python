from dataclasses import dataclass, field
from typing import Optional

from scheme.org.eidr.schema.active_filter_type import ActiveFilterType
from scheme.org.eidr.schema.administrator_type_type import (
    AdministratorTypeType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class PartyQueryType:
    class Meta:
        name = "partyQueryType"

    party_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartyName",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    role_filter: list[AdministratorTypeType] = field(
        default_factory=list,
        metadata={
            "name": "RoleFilter",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "max_occurs": 7,
        },
    )
    active_filter: ActiveFilterType = field(
        default=ActiveFilterType.ALL,
        metadata={
            "name": "ActiveFilter",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    page_number: int = field(
        default=1,
        metadata={
            "name": "PageNumber",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    page_size: int = field(
        default=20,
        metadata={
            "name": "PageSize",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    continuation_token: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContinuationToken",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
