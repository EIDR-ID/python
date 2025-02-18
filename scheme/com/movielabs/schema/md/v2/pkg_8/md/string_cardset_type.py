from enum import Enum

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


class StringCardsetType(Enum):
    ANTI_PIRACY = "AntiPiracy"
    DISTRIBUTION_LOGO = "DistributionLogo"
    DUBBING_CREDIT = "DubbingCredit"
    EDIT_NOTICE = "EditNotice"
    HEALTH = "Health"
    INTERMISSION = "Intermission"
    RATING = "Rating"
    OTHER = "Other"
