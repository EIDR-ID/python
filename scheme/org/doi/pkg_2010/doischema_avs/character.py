from enum import Enum

__NAMESPACE__ = "http://www.doi.org/2010/DOISchemaAVS"


class Character(Enum):
    """Allowed values for the types of character in which the content of a
    referentCreation may be expressed.

    The values in this element are drawn from the RDA/ONIX Framework for
    Resource Categorization.

    :cvar IMAGE: Content expressed in line, shape, mass and/or other
        visually-realized forms.
    :cvar LANGUAGE: Content expressed in human or machine-readable
        language.
    :cvar MUSIC: Content expressed in musical notes.
    :cvar OTHER: Content expressed in a form other than language, music,
        or image. 'Other' includes other forms of communicating
        phenomena, qualities, etc., perceived directly through the human
        senses (for example, natural or machine-generated sounds,
        aromas, textures as well as those that cannot be perceived
        directly through the human senses (for example, electromagnetic
        waves).
    :cvar RESTRICTED: A Creation identified within a restricted DOI
        Application Profile for which kernel metadata values are not
        generally available.
    """

    IMAGE = "Image"
    LANGUAGE = "Language"
    MUSIC = "Music"
    OTHER = "Other"
    RESTRICTED = "Restricted"
