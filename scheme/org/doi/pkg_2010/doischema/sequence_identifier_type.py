from dataclasses import dataclass, field
from typing import Optional

from scheme.org.doi.pkg_2010.doischema_avs.sequence_identifier_type import (
    SequenceIdentifierType as SequenceIdentifierTypeSequenceIdentifierType,
)

__NAMESPACE__ = "http://www.doi.org/2010/DOISchema"


@dataclass
class SequenceIdentifierType:
    """
    A complex element describing the type of an identifier used to identify the
    order of a relationship between two entities.

    :ivar value:
    :ivar user_defined_type: The type of the sequenceIdentifier if the
        sequenceIdentifierType is 'ProprietaryIdentifier'.
    :ivar valid_namespace: The namespace of the sequenceIdentifier if
        the sequenceIdentifierType is 'ProprietaryIdentifier'.
    :ivar governing_party: The name or identifier of the party
        ultimately responsible for issuing the sequenceIdentifier if the
        sequenceIdentifierType is 'ProprietaryIdentifier'.
    """

    class Meta:
        name = "sequenceIdentifierType"

    value: Optional[SequenceIdentifierTypeSequenceIdentifierType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    user_defined_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "userDefinedType",
            "type": "Attribute",
        },
    )
    valid_namespace: Optional[str] = field(
        default=None,
        metadata={
            "name": "validNamespace",
            "type": "Attribute",
        },
    )
    governing_party: Optional[str] = field(
        default=None,
        metadata={
            "name": "governingParty",
            "type": "Attribute",
        },
    )
