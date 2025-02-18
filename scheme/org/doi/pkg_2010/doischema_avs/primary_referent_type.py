from enum import Enum

__NAMESPACE__ = "http://www.doi.org/2010/DOISchemaAVS"


class PrimaryReferentType(Enum):
    """
    Allowed values for the primary type of a referent.

    :cvar CREATION: A Resource made, directly or indirectly, by one or
        more human beings.
    :cvar PARTY: An individual person, animal or organization capable of
        acting, or being perceived to act, as an agent. Parties may be
        real, legendary or imaginary, and do not need to be biologically
        unique. Personas adopted for artistic or other purposes may be
        referenced with DOIs as unique individuals. For example, the
        authors 'Ellis Peters' 'John Redfern' 'Jolyon Carr' and 'Peter
        Benedict' may be identified as a unique parties distinct from
        the person 'Edith Pargeter', for whom they are all pen-name
        pseudonyms. 'Mickey Mouse' may be identified as an individual
        for the purpose of unique identification as a performer in a
        creation, or 'Borat' or 'Hamlet' for the identification of a
        character depicted in a fictional work.
    """

    CREATION = "Creation"
    PARTY = "Party"
