from enum import Enum

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


class BasicMetadataParentTypeRelationshipType(Enum):
    ISCLIPOF = "isclipof"
    ISEPISODEOF = "isepisodeof"
    ISSEASONOF = "isseasonof"
    ISPIECEOF = "ispieceof"
    ISPARTOF = "ispartof"
    ISDERIVEDFROM = "isderivedfrom"
    ISCOMPOSITEOF = "iscompositeof"
    ISSUPPLEMENTTO = "issupplementto"
    ISPROMOTIONFOR = "ispromotionfor"
