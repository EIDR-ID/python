from dataclasses import dataclass, field
from typing import Optional

from app.scheme.org.doi.pkg_2010.doischema.creation_identifier_type import (
    CreationIdentifierType,
)
from app.scheme.org.doi.pkg_2010.doischema.uri import Uri

__NAMESPACE__ = "http://www.doi.org/2010/DOISchema"


@dataclass
class CreationIdentifier:
    """A complex element describing an identifier used to identify a creation.

    An identifier is a type of name of which each instance is unique of its type: for example , the ISBN '9780946014491' belongs to only one book.

    :ivar value: The value of the Identifier. This element is deprecated
        and not to be used in XML data conforming to the current XSD
        version. It is only included to ensure that data conforming to
        the earlier XSD version remains valid and will be removed at a
        future date.
    :ivar non_uri_value: The value of the creationIdentifier if it is
        not a URI.
    :ivar uri: The value of the creationIdentifier if it is a URI.
    :ivar type_value: The type of the creationIdentifier.
    """

    class Meta:
        name = "creationIdentifier"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.doi.org/2010/DOISchema",
        },
    )
    non_uri_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "nonUriValue",
            "type": "Element",
            "namespace": "http://www.doi.org/2010/DOISchema",
        },
    )
    uri: list[Uri] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.doi.org/2010/DOISchema",
        },
    )
    type_value: Optional[CreationIdentifierType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.doi.org/2010/DOISchema",
            "required": True,
        },
    )
