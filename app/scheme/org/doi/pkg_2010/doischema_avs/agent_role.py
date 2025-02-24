from enum import Enum

__NAMESPACE__ = "http://www.doi.org/2010/DOISchemaAVS"


class AgentRole(Enum):
    """Allowed values for roles played by a party as an agent of a Creation.

    This is an open set. Other values may be registered with the IDF by
    any Registration Authority.

    :cvar ACTOR: A Performer of spoken (and sometimes silent) dramatic
        roles.
    :cvar AUTHOR: A Creator of a lexical work (words).
    :cvar COMPOSER: A Creator of a musical work.
    :cvar CORPORATE_CREATOR: An Organization credited as a Creator of a
        Creation.
    :cvar CREATOR: A creator of a Creation. This is a generic value
        which may be used when a more appropriate specific role (such as
        author or composer) is not available.
    :cvar DIRECTOR: A person responsible for the direction of Performers
        and other creative elements of a Creation.
    :cvar PUBLISHER: A Party making a Creation available to the public.
    """

    ACTOR = "Actor"
    AUTHOR = "Author"
    COMPOSER = "Composer"
    CORPORATE_CREATOR = "CorporateCreator"
    CREATOR = "Creator"
    DIRECTOR = "Director"
    PUBLISHER = "Publisher"
