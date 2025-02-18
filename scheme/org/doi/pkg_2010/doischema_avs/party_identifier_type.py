from enum import Enum

__NAMESPACE__ = "http://www.doi.org/2010/DOISchemaAVS"


class PartyIdentifierType(Enum):
    """Allowed values for types of partyIdentifier.

    This is an open set. Other values may be registered with the IDF by
    any Registration Authority.

    :cvar DOI: A DOI Name issued under the authority of the
        International DOI Foundation.
    :cvar EIDRPARTY_ID: An EIDR ID which identifies a Party.
    :cvar IPNUMBER: An Interested Party Number, an identifier for
        Parties issued under the governance of CISAC. Formerly known as
        the CAE (Compositeur, Auteur, Editeur) Number.
    :cvar ISNI: An International Standard Name Identifier, the ISO
        Standard Identifier for Parties as defined in ISO 27729.
    :cvar PROPRIETARY_IDENTIFIER: An Identifier from a scheme which is
        proprietary to a particular party.
    """

    DOI = "DOI"
    EIDRPARTY_ID = "EIDRPartyID"
    IPNUMBER = "IPNumber"
    ISNI = "ISNI"
    PROPRIETARY_IDENTIFIER = "ProprietaryIdentifier"
