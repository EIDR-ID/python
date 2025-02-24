from enum import Enum

__NAMESPACE__ = "http://www.doi.org/2010/DOISchemaAVS"


class SequenceIdentifierType(Enum):
    """Allowed values for types of sequenceIdentifier.

    This is an open set. Other values may be registered with the IDF by
    any Registration Authority.

    :cvar PAGE_NUMBER: A SequenceIdentifier identifying a page in a
        containing creation, e.g. in a book or in a journal, on which a
        contained creation, e.g. a chapter or an article, starts.
    :cvar PROPRIETARY_IDENTIFIER: An Identifier from a scheme which is
        proprietary to a particular party.
    """

    PAGE_NUMBER = "PageNumber"
    PROPRIETARY_IDENTIFIER = "ProprietaryIdentifier"
