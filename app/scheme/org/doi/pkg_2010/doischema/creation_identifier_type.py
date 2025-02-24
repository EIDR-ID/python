from dataclasses import dataclass, field
from typing import Optional

from app.scheme.org.doi.pkg_2010.doischema_avs.creation_identifier_type import (
    CreationIdentifierType as CreationIdentifierTypeCreationIdentifierType,
)

__NAMESPACE__ = "http://www.doi.org/2010/DOISchema"


@dataclass
class CreationIdentifierType:
    """
    A complex element describing the type of an identifier used to identify a
    creation.

    :ivar value:
    :ivar user_defined_type: The type of the creationIdentifier if the
        creationIdentifierType is 'ProprietaryIdentifier'.
    :ivar valid_namespace: The namespace of the creationIdentifier if
        the creationIdentifierType is 'ProprietaryIdentifier'.
    :ivar governing_party: The name or identifier of the party
        ultimately responsible for issuing the creationIdentifier if the
        creationIdentifierType is 'ProprietaryIdentifier'.
    """

    class Meta:
        name = "creationIdentifierType"

    value: Optional[CreationIdentifierTypeCreationIdentifierType] = field(
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
