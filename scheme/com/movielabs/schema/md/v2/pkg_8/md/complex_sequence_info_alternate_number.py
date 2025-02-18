from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class ComplexSequenceInfoAlternateNumber:
    """
    Domain attribute is required for AlternateNumber.
    """

    class Meta:
        name = "complex-SequenceInfo-AlternateNumber"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 8,
            "pattern": r"[0-9a-zA-Z]+([:/\-.,][0-9a-zA-Z]+)*",
        },
    )
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
