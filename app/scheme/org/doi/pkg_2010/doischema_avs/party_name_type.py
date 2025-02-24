from enum import Enum

__NAMESPACE__ = "http://www.doi.org/2010/DOISchemaAVS"


class PartyNameType(Enum):
    """Allowed values for types of partyName.

    This is an open set. Other values may be registered with the IDF by
    any Registration Authority.

    :cvar ABBREVIATED_NAME: A shortened form of a Name (which may be an
        acronym, in whole or in part) by which a party is known.
    :cvar FORMER_NAME: A Name by which a party was previously known.
    :cvar NAME: A Name by which a party is known.
    :cvar PRINCIPAL_NAME: The Name by which a party is principally
        known.
    """

    ABBREVIATED_NAME = "AbbreviatedName"
    FORMER_NAME = "FormerName"
    NAME = "Name"
    PRINCIPAL_NAME = "PrincipalName"
