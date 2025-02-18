from enum import Enum

__NAMESPACE__ = "http://www.doi.org/2010/DOISchemaAVS"


class CreationStructuralType(Enum):
    """
    Allowed values for a structuralType of a Creation.

    :cvar ABSTRACTION: A Creation which exists as a concept and is
        recognised only through one more more physical, digital or
        spatio-temporal Manifestations. An abstraction (sometimes known
        as a 'work' or 'abstract work') represents the content of a
        creation, regardless of the carrier or media in which it is
        expressed. For example, the play 'Hamlet' is an abstraction
        which has been expressed in many performances, printed books,
        films, broadcasts and more recently in digital media.
    :cvar DIGITAL: A Creation which is expressed in digital form. A
        digital creation is entirely made of digital bits and so may be
        perceived only through a computer or other intermediary device.
        For example, an audio CD is not itself a digital creation but a
        physical one, but it contains several digital creations (the
        individual tracks).
    :cvar PERFORMANCE: A Creation which is expressed in a transient
        form. A performance describes a 'spatio-temporal' creation, such
        as a speech, a play or the playing of a piece of music. It may
        be recorded for reproduction, but the creation itself is only
        perceivable in transient form.
    :cvar PHYSICAL: A Creation which is expressed in physical form.
    :cvar RESTRICTED: A Creation identified within a restricted DOI
        Application Profile for which kernel metadata values are not
        generally available.
    """

    ABSTRACTION = "Abstraction"
    DIGITAL = "Digital"
    PERFORMANCE = "Performance"
    PHYSICAL = "Physical"
    RESTRICTED = "Restricted"
