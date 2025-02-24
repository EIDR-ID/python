from dataclasses import dataclass, field
from typing import Optional

from app.scheme.org.doi.pkg_2010.doischema_avs.creation_name_type import (
    CreationNameType,
)

__NAMESPACE__ = "http://www.doi.org/2010/DOISchema"


@dataclass
class CreationName:
    """A complex element describing a name or title by which a creation is known.

    The distinction between 'name' and 'title' is a matter of
    convention: published creations such as books, serials, CDs, DVDs or
    broadcast programmes normally have 'titles', but other creations
    such as websites or datasets more commonly have 'names'. There is no
    functional difference.

    :ivar value: The text string representing the value of the
        creationName.
    :ivar subname_value: A text string representing a subname or
        subtitle which accompanies the creationName. This is not an
        alternative name for the creation which may be used
        independently, but a name or subtitle which supports the main
        creationName. For example, the book titled 'Knowledge
        Representation' by John F. Sowa has the subtitle 'Logical,
        Philosophical and Computational Foundations'.
    :ivar type_value: The type of the creationName.
    :ivar primary_language: The primary language in which the
        creationName is expressed.
    """

    class Meta:
        name = "creationName"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.doi.org/2010/DOISchema",
            "required": True,
        },
    )
    subname_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "subnameValue",
            "type": "Element",
            "namespace": "http://www.doi.org/2010/DOISchema",
        },
    )
    type_value: Optional[CreationNameType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.doi.org/2010/DOISchema",
            "required": True,
        },
    )
    primary_language: Optional[str] = field(
        default=None,
        metadata={
            "name": "primaryLanguage",
            "type": "Attribute",
        },
    )
