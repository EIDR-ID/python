from enum import Enum

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


class StringVideoEncVbr(Enum):
    VBR = "VBR"
    CONSTRAINED_VBR = "Constrained VBR"
    VALUE_2_PASS_VBR = "2-pass VBR"
