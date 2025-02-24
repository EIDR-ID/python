from dataclasses import dataclass, field
from typing import Optional

from app.scheme.org.doi.pkg_2010.doischema_avs.return_type import ReturnType

__NAMESPACE__ = "http://www.doi.org/2010/DOISchema"


@dataclass
class Uri:
    """
    A complex element describing an URI used to identify a creation.

    :ivar value:
    :ivar return_type: The type (MIME type or equivalent) of the page
        that is returned by the URI.
    :ivar does_content_negotiation: A flag that identifies the URI that
        does content negotiation (whose returnType acts as the default).
    """

    class Meta:
        name = "uri"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    return_type: Optional[ReturnType] = field(
        default=None,
        metadata={
            "name": "returnType",
            "type": "Attribute",
        },
    )
    does_content_negotiation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "doesContentNegotiation",
            "type": "Attribute",
        },
    )
