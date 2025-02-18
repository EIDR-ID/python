from dataclasses import dataclass, field
from typing import Optional

from scheme.org.doi.pkg_2010.doischema.creation_identifier import (
    CreationIdentifier,
)
from scheme.org.doi.pkg_2010.doischema.creation_name import CreationName
from scheme.org.doi.pkg_2010.doischema.linked_creation import LinkedCreation
from scheme.org.doi.pkg_2010.doischema.principal_agent import PrincipalAgent
from scheme.org.doi.pkg_2010.doischema_avs.character import Character
from scheme.org.doi.pkg_2010.doischema_avs.creation_structural_type import (
    CreationStructuralType,
)
from scheme.org.doi.pkg_2010.doischema_avs.creation_type import CreationType
from scheme.org.doi.pkg_2010.doischema_avs.mode import Mode

__NAMESPACE__ = "http://www.doi.org/2010/DOISchema"


@dataclass
class ReferentCreation:
    """
    A complex element describing the creation identified by the doiName to which
    the kernelMetadata applies.

    :ivar name: A name or title by which the referentCreation is known.
        For Kernel Metadata in a restricted Application Profile the
        string 'No information available' should be used, with a
        creationNameType of 'name'.
    :ivar identifier: An identifier of the referentCreation.
    :ivar structural_type: The primary structuralType of a
        referentCreation. For creations there are four mutually
        exclusive structuralTypes (physical, digital, performance and
        abstraction) that allow classification according to overall
        form. Where structuralTypes may be contained within one another,
        the referent's structuralType is defined by the overall form.
        For example a CD (physical) may contain files (digital) which
        contain recordings of performances of songs (abstractions), and
        elements of content can be further classified if necessary under
        referentType.
    :ivar mode: A principal sensory mode in which a referentCreation is
        intended to be perceived (audio, visual, tangible, olfactory,
        tasteable, none). Mode identifies only the principal intended
        modes of perception: most physical creations are perceivable
        with all five senses, but some of these perceptions may be
        trivial. For example, a printed book may be touched or smelled,
        but these are normally supplementary or incidental to the visual
        mode for its intended function as a content carrier. For a
        Braille book, however, touch would be a principal mode. One
        creation may be perceived in several modes (audio and visual
        being much the most common combination).
    :ivar character: A fundamental form of communication (language,
        music, image, other) in which the content of a referentCreation
        is expressed.
    :ivar type_value: A class of creation to which the referentCreation
        belongs.
    :ivar principal_agent: A party (either an individual or an
        organization) principally responsible for the creation or
        publication of the referentCreation.
    :ivar linked_creation: Another creation with which the
        referentCreation is associated.
    """

    class Meta:
        name = "referentCreation"

    name: list[CreationName] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.doi.org/2010/DOISchema",
            "min_occurs": 1,
        },
    )
    identifier: list[CreationIdentifier] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.doi.org/2010/DOISchema",
        },
    )
    structural_type: Optional[CreationStructuralType] = field(
        default=None,
        metadata={
            "name": "structuralType",
            "type": "Element",
            "namespace": "http://www.doi.org/2010/DOISchema",
            "required": True,
        },
    )
    mode: list[Mode] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.doi.org/2010/DOISchema",
            "min_occurs": 1,
        },
    )
    character: list[Character] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.doi.org/2010/DOISchema",
            "min_occurs": 1,
        },
    )
    type_value: list[CreationType] = field(
        default_factory=list,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.doi.org/2010/DOISchema",
            "min_occurs": 1,
        },
    )
    principal_agent: list[PrincipalAgent] = field(
        default_factory=list,
        metadata={
            "name": "principalAgent",
            "type": "Element",
            "namespace": "http://www.doi.org/2010/DOISchema",
            "min_occurs": 1,
        },
    )
    linked_creation: list[LinkedCreation] = field(
        default_factory=list,
        metadata={
            "name": "linkedCreation",
            "type": "Element",
            "namespace": "http://www.doi.org/2010/DOISchema",
        },
    )
