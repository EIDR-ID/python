from dataclasses import dataclass, field
from typing import Optional

from scheme.org.eidr.schema.alternate_idtype import AlternateIdtype
from scheme.org.eidr.schema.linked_alternate_idurltype import (
    LinkedAlternateIdurltype,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class LinkedAlternateIdtype:
    """
    An AlternateID together with 0 or more URL elements.
    """

    class Meta:
        name = "linkedAlternateIDType"

    alternate_id: Optional[AlternateIdtype] = field(
        default=None,
        metadata={
            "name": "AlternateID",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    url: list[LinkedAlternateIdurltype] = field(
        default_factory=list,
        metadata={
            "name": "URL",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
