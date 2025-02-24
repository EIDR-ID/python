from dataclasses import dataclass, field
from typing import Optional

from    .alternate_idtype import AlternateIdtype

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class Proprietary(AlternateIdtype):
    """Any value allowed.

    Required attribute for domain of reference, e.g.
    "<AlternateID xmlns="" xmlns:xs="http://www.w3.org/2001/XMLSchema" xs:type="{http://www.eidr.org/schema}Proprietary" domain="http://www.colossalcave.com">XYZZY</AlternateID>"
    """

    domain: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 256,
            "pattern": r"[\S]+[.][\S]+",
        },
    )
