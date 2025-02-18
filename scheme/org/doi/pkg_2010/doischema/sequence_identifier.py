from dataclasses import dataclass, field
from typing import Optional

from scheme.org.doi.pkg_2010.doischema.sequence_identifier_type import (
    SequenceIdentifierType,
)

__NAMESPACE__ = "http://www.doi.org/2010/DOISchema"


@dataclass
class SequenceIdentifier:
    """
    A complex element describing an identifier used to identify the order of a
    relationship between two entities.

    :ivar value: A text string representing the value of the
        sequenceIdentifier (for example, '1A').
    :ivar type_value: The type of the sequenceIdentifier.
    """

    class Meta:
        name = "sequenceIdentifier"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.doi.org/2010/DOISchema",
            "required": True,
        },
    )
    type_value: Optional[SequenceIdentifierType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.doi.org/2010/DOISchema",
            "required": True,
        },
    )
