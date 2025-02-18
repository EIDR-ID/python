from dataclasses import dataclass, field
from typing import Optional

from scheme.org.eidr.schema.alternate_idrelation_type import (
    AlternateIdrelationType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class AlternateIdtype:
    """Since this is abstract, any field using it has to provide one of the
    derived types as an xsi:type attribute, e.g.
    "<AlternateID xmlns="" xmlns:xs="http://www.w3.org/2001/XMLSchema" xs:type="{http://www.eidr.org/schema}DOI">10.123/456</AlternateID>"
    This would be easier (and more controlled) under W3C
    schema 1.1 using conditional type assignment.
    Note: xs: in the example above should be xsi: but some validators don't like that unless the namespace is declared,
    even inside the documentation element."""

    class Meta:
        name = "alternateIDType"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 1024,
        },
    )
    relation: Optional[AlternateIdrelationType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
