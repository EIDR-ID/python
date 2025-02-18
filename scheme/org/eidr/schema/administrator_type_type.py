from enum import Enum

__NAMESPACE__ = "http://www.eidr.org/schema"


class AdministratorTypeType(Enum):
    """
    See Chapter 7 of the spec for details on these.

    :cvar ASSOCIATED_ORG: Identifies a party that can be listed as an
        AssociatedOrg for an asset.
    :cvar REGISTRANT: Identifies a party that is registering or has
        registered a work
    :cvar METADATA_AUTHORITY: Identifies a party who has asserted that
        they possess complete and correct metadata for the record and
        who has agreed to maintain the record.
    :cvar ENCODING_AGENT: Identifies a partythat can be listed as
        EncodingAgent for a regustered encoding
    :cvar WRITER: Identifies a party that can write to objects, but not
        create, delete, or promote them -- e.g. a clean-up crew
    :cvar READER: Identifies a party that is allowed to see information
        that would otherwise be hidden
    :cvar SERVICE_ADMIN: Identifies a party that is allowed to create,
        modify, delete, or alias video services information
    :cvar ALT_IDWRITER: Identifies a party that is allowed to modify
        AlternateID information on any record
    """

    ASSOCIATED_ORG = "AssociatedOrg"
    REGISTRANT = "Registrant"
    METADATA_AUTHORITY = "MetadataAuthority"
    ENCODING_AGENT = "EncodingAgent"
    WRITER = "Writer"
    READER = "Reader"
    SERVICE_ADMIN = "ServiceAdmin"
    ALT_IDWRITER = "AltIDWriter"
