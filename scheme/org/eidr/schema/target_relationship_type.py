from enum import Enum

__NAMESPACE__ = "http://www.eidr.org/schema"


class TargetRelationshipType(Enum):
    COMPOSITE_RELATIONSHIP = "CompositeRelationship"
    PACKAGING_RELATIONSHIP = "PackagingRelationship"
    SUPPLEMENTAL_RELATIONSHIP = "SupplementalRelationship"
    PROMOTIONAL_RELATIONSHIP = "PromotionalRelationship"
    ALTERNATE_CONTENT_RELATIONSHIP = "AlternateContentRelationship"
