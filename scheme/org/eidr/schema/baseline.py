from dataclasses import dataclass

from scheme.org.eidr.schema.alternate_idtype import AlternateIdtype

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class Baseline(AlternateIdtype):
    """This is an ID from the Project ID space, which covers Film, TV, Season,
    Episode, and DVD.

    To use this ID within the Baseline system you may need to look at
    the EIDR ReferentType and/or the Baseline IDs of any ancestors.
    """
