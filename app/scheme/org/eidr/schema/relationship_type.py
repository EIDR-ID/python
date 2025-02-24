from enum import Enum

__NAMESPACE__ = "http://www.eidr.org/schema"


class RelationshipType(Enum):
    IS_SEASON_OF = "isSeasonOf"
    IS_EPISODE_OF = "isEpisodeOf"
    IS_EDIT_OF = "isEditOf"
    IS_MANIFESTATION_OF = "isManifestationOf"
    IS_CLIP_OF = "isClipOf"
    IS_COMPOSITE_OF = "isCompositeOf"
    IS_COMPILATION_OF = "isCompilationOf"
    IS_PACKAGING_OF = "isPackagingOf"
    IS_PROMOTION_FOR = "isPromotionFor"
    IS_SUPPLEMENT_TO = "isSupplementTo"
    IS_ALTERNATE_CONTENT_FOR = "isAlternateContentFor"
