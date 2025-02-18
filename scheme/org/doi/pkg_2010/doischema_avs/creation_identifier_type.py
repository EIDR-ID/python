from enum import Enum

__NAMESPACE__ = "http://www.doi.org/2010/DOISchemaAVS"


class CreationIdentifierType(Enum):
    """Allowed values for types of creationIdentifier.

    This is an open set. Other values may be registered with the IDF by
    any Registration Authority.

    :cvar AD_ID: An Ad-ID, a 12-character identifier used by the
        advertising industry for identifying advertising assets,
        described at www.ad-id.org.
    :cvar AMG: An All Media Guide Identifier, an identifier for entities
        (artists, music, etc.) in the AMG database now maintained by
        Rovi.
    :cvar BASELINE: A Baseline Identifier, a 7-digit identifier for
        audiovisual works.
    :cvar C_IDF: A Content ID Forum Identifier (version 2.0 rev 1.1),
        specified at http://www.npo-ba.org/cid/cIDfSpecV2R11E.pdf.
    :cvar CRID: A Content Reference Identifier, an URI for content
        created by the TV-Anytime forum and described in RFC 4078.
    :cvar DOI: A DOI Name issued under the authority of the
        International DOI Foundation.
    :cvar EAN13: An International Article Number (formerly European
        Article Number), a 13-digit identifier for products.
    :cvar EDITION_NUMBER: An Identifier of a Creation which denotes its
        edition.
    :cvar EIDR_CONTENT_ID: An EIDR ID which identifies a Creation.
    :cvar GRID: A Global Release Identifier, an 18-character identifier
        for releases of music over electronic networks as defined by
        IFPI.
    :cvar IMDB_ID: An Internet Movie Database (IMDb) Movie ID, a 7-digit
        identifier for AudiovisualWorks issued by the IMDb.
    :cvar ISAN: An International Standard Audiovisual Number, the ISO
        Standard Identifier for AudiovisualWorks as defined in ISO
        15706.
    :cvar ISBN10: An International Standard Book Number, the ISO
        Standard Identifier for books as defined in ISO 2108, in its
        10-digit form. The isbn10 is now deprecated but is included in
        this schema for legacy purposes.
    :cvar ISBN13: An International Standard Book Number, the ISO
        Standard Identifier for books as defined in ISO 2108, in its
        13-digit form.
    :cvar ISRC: An International Standard Recording Code, the ISO
        Standard Identifier for SoundRecordings as defined in ISO 3901.
    :cvar ISSN: An International Standard Serial Number, the ISO
        Standard Identifier for published Serials as defined in ISO
        3297.
    :cvar ISTC: An International Standard Text Code, the ISO Standard
        Identifier for textual works as defined in ISO 21047.
    :cvar ISWC: An International Standard Musical Work Code, the ISO
        Standard Identifier for musical works as defined in ISO 15707.
    :cvar IVA: An Internet Video Archive Identifier, a 7-digit
        identifier for trailers, defined by the Internet Video Archive.
    :cvar MUZE: A MUZE Identifier, an 8-character identifier for music
        songs in the MUZE database now maintained by Rovi.
    :cvar PII: A Publisher Item Identifier, a 17-character identifier
        based on ISSN and ISBN that is used commonly by publishers for
        journal articles.
    :cvar PROPRIETARY_IDENTIFIER: An Identifier from a scheme which is
        proprietary to a particular party.
    :cvar SMPTE_UMID: A Unique Material Identifier, a 32-byte identifier
        for audiovisual Creations as defined in  SMPTE 330M-2004.
    :cvar TRIB: A Tribune Media Services Unique ID, a 14-character
        identifier for audiovisual works.
    :cvar TVG: A TV Guide Identifier, a 6-digit identifier for televised
        audiovisual works.
    :cvar UPC: A Universal Product Code, a 12-digit identifier for
        products.
    :cvar URI: A Uniform Resource Identifier, an identifier for
        WebResources as defined in IETF's RFC 3986.
    :cvar URN: A Uniform Resource Name, an identifier for WebResources
        as defined in IETF's RFC 2141.
    :cvar UUID: A Universally Unique Identifier, an identifier with 32
        hexadecimal digits for [Resources] described in  ITU-T Rec.
        X.667 and IETF RFC 4122.
    """

    AD_ID = "Ad-ID"
    AMG = "AMG"
    BASELINE = "Baseline"
    C_IDF = "cIDF"
    CRID = "CRID"
    DOI = "DOI"
    EAN13 = "EAN13"
    EDITION_NUMBER = "EditionNumber"
    EIDR_CONTENT_ID = "EidrContentID"
    GRID = "GRid"
    IMDB_ID = "IMDbID"
    ISAN = "ISAN"
    ISBN10 = "ISBN10"
    ISBN13 = "ISBN13"
    ISRC = "ISRC"
    ISSN = "ISSN"
    ISTC = "ISTC"
    ISWC = "ISWC"
    IVA = "IVA"
    MUZE = "MUZE"
    PII = "PII"
    PROPRIETARY_IDENTIFIER = "ProprietaryIdentifier"
    SMPTE_UMID = "SMPTE-UMID"
    TRIB = "TRIB"
    TVG = "TVG"
    UPC = "UPC"
    URI = "URI"
    URN = "URN"
    UUID = "UUID"
