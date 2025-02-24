from enum import Enum

__NAMESPACE__ = "http://www.doi.org/2010/DOISchemaAVS"


class AssociatedPartyRole(Enum):
    """Allowed values for a role associated with a party.

    This is an open set. Other values may be registered with the IDF by
    any Registration Authority.

    :cvar AUTHOR: A party known as a creator of lexical works (words).
    :cvar BOOK_PUBLISHER: A party known for publishing books.
    :cvar COMPOSER: A party known as a creator of musical works.
    :cvar CORPORATE_CREATOR: An organization known for being credited as
        a creator of creations.
    :cvar CREATOR: A party known as a creator of creations. This is a
        generic value which may be used when a more appropriate specific
        role (such as author or composer) is not available.
    :cvar DIGITAL_SERVICE_PROVIDER: A party known for providing digital
        content through the internet, a telecom network or other means
        of carrier-less delivery.
    :cvar JOURNAL_PUBLISHER: A party known for publishing journals.
    :cvar VIDEO_SERVICE_PROVIDER: A party known for providing scheduled
        or on-demand video services (for example, audiovisual content
        delivered through tv, satellite, cable or internet media).
    """

    AUTHOR = "Author"
    BOOK_PUBLISHER = "BookPublisher"
    COMPOSER = "Composer"
    CORPORATE_CREATOR = "CorporateCreator"
    CREATOR = "Creator"
    DIGITAL_SERVICE_PROVIDER = "DigitalServiceProvider"
    JOURNAL_PUBLISHER = "JournalPublisher"
    VIDEO_SERVICE_PROVIDER = "VideoServiceProvider"
