from enum import Enum

__NAMESPACE__ = "http://www.doi.org/2010/DOISchemaAVS"


class CreationNameType(Enum):
    """Allowed Values for types of creationName.

    This is an open set. Other values may be registered with the IDF by
    any Registration Authority.

    :cvar ABBREVIATED_TITLE: A Title which is a shortened form of
        another Title.
    :cvar DISTINCTIVE_TITLE: The Title by which a Creation is normally
        known.
    :cvar FORMER_TITLE: A Title by which a Creation was once known.
    :cvar NAME: A Name of a Creation.
    :cvar TITLE: A Title of a Creation.
    :cvar TRANSLATED_TITLE: A Title which is a translation of another
        Title.
    """

    ABBREVIATED_TITLE = "AbbreviatedTitle"
    DISTINCTIVE_TITLE = "DistinctiveTitle"
    FORMER_TITLE = "FormerTitle"
    NAME = "Name"
    TITLE = "Title"
    TRANSLATED_TITLE = "TranslatedTitle"
