from dataclasses import dataclass, field
from typing import Optional

from scheme.org.doi.pkg_2010.doischema.creation_identifier import (
    CreationIdentifier,
)
from scheme.org.doi.pkg_2010.doischema.creation_name import CreationName
from scheme.org.doi.pkg_2010.doischema.sequence_identifier import (
    SequenceIdentifier,
)
from scheme.org.doi.pkg_2010.doischema_avs.creation_to_creation_link_role import (
    CreationToCreationLinkRole,
)

__NAMESPACE__ = "http://www.doi.org/2010/DOISchema"


@dataclass
class LinkedCreation:
    """A complex element describing another creation with which the
    referentCreation is associated.

    At least one of the elements 'creationName' or 'creationIdentifier'
    must be present (the latter being preferably a doiName), and at
    least one of the elements 'referentCreationRole' or
    'linkedCreationRole'.

    :ivar name: A name or title by which the linkedCreation is known.
    :ivar identifier: An identifier of the linkedCreation.
    :ivar referent_creation_role: A role played by the referentCreation
        in relation to the linkedCreation (for example, the
        referentCreation is an edition of the linkedCreation).
    :ivar linked_creation_role: A role played by the linkedCreation in
        relation to the referentCreation (for example, the
        linkedCreation is an edition of the referentCreation).
    :ivar referent_creation_sequence_identifier: An identifier of the
        referentCreation, giving the order in which it appears within a
        list of creations linked to the linkedCreation.
    :ivar linked_creation_sequence_identifier: An identifier of the
        linkedCreation, giving the order in which it appears within a
        list of creations linked to the referentCreation.
    """

    class Meta:
        name = "linkedCreation"

    name: list[CreationName] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.doi.org/2010/DOISchema",
        },
    )
    identifier: list[CreationIdentifier] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.doi.org/2010/DOISchema",
        },
    )
    referent_creation_role: Optional[CreationToCreationLinkRole] = field(
        default=None,
        metadata={
            "name": "referentCreationRole",
            "type": "Element",
            "namespace": "http://www.doi.org/2010/DOISchema",
        },
    )
    linked_creation_role: Optional[CreationToCreationLinkRole] = field(
        default=None,
        metadata={
            "name": "linkedCreationRole",
            "type": "Element",
            "namespace": "http://www.doi.org/2010/DOISchema",
        },
    )
    referent_creation_sequence_identifier: list[SequenceIdentifier] = field(
        default_factory=list,
        metadata={
            "name": "referentCreationSequenceIdentifier",
            "type": "Element",
            "namespace": "http://www.doi.org/2010/DOISchema",
        },
    )
    linked_creation_sequence_identifier: list[SequenceIdentifier] = field(
        default_factory=list,
        metadata={
            "name": "linkedCreationSequenceIdentifier",
            "type": "Element",
            "namespace": "http://www.doi.org/2010/DOISchema",
        },
    )
