from enum import Enum

__NAMESPACE__ = "http://www.eidr.org/schema"


class ResolutionTypeType(Enum):
    DOIKERNEL = "DOIKernel"
    FULL = "Full"
    SELF_DEFINED = "SelfDefined"
    SIMPLE = "Simple"
    PROVENANCE = "Provenance"
    INHERITED = "Inherited"
