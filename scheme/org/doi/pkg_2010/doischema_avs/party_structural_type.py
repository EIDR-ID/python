from enum import Enum

__NAMESPACE__ = "http://www.doi.org/2010/DOISchemaAVS"


class PartyStructuralType(Enum):
    """
    Allowed values for the primary type of a referent.

    :cvar ANIMAL: A non-human animal. Animals may require identification
        for many reasons: for example, as performers ('Lassie').
    :cvar INDIVIDUAL: An individual human being, real or imaginary, or
        an imaginary Party attributed with characteristics of a human
        being (for example, Homer Simpson, Mickey Mouse). Individuals
        may be real, legendary or imaginary, and do not need to be
        biologically unique. Personas adopted for artistic or other
        purposes may be referenced with DOIs as unique individuals. For
        example, the authors 'Ellis Peters' 'John Redfern' 'Jolyon Carr'
        and 'Peter Benedict' may be identified as a unique parties
        distinct from the person 'Edith Pargeter', for whom they are all
        pen-name pseudonyms. 'Mickey Mouse' may be identified as an
        individual for the purpose of unique identification as a
        performer in a creation, or 'Borat' or 'Hamlet' for the
        identification of a character depicted in a fictional work.
    :cvar ORGANIZATION: A Party which is either a legal person such as a
        corporation or legal partnership (but not a human being); or a
        group of Individuals, or a group of organizations. Organizations
        include all groupings of two or more parties, as well as legally
        defined, non-human parties.
    """

    ANIMAL = "Animal"
    INDIVIDUAL = "Individual"
    ORGANIZATION = "Organization"
