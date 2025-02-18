from dataclasses import dataclass, field
from typing import Optional

from scheme.com.movielabs.schema.md.v2.pkg_8.md.complex_sequence_info_alternate_number import (
    ComplexSequenceInfoAlternateNumber,
)
from scheme.com.movielabs.schema.md.v2.pkg_8.md.complex_sequence_info_distribution_number import (
    ComplexSequenceInfoDistributionNumber,
)
from scheme.com.movielabs.schema.md.v2.pkg_8.md.complex_sequence_info_house_sequence import (
    ComplexSequenceInfoHouseSequence,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class ContentSequenceInfoType:
    """
    Restrict cardinalities, remove Number Element.
    """

    class Meta:
        name = "ContentSequenceInfo-type"

    distribution_number: Optional[ComplexSequenceInfoDistributionNumber] = (
        field(
            default=None,
            metadata={
                "name": "DistributionNumber",
                "type": "Element",
                "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            },
        )
    )
    house_sequence: Optional[ComplexSequenceInfoHouseSequence] = field(
        default=None,
        metadata={
            "name": "HouseSequence",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    alternate_number: list[ComplexSequenceInfoAlternateNumber] = field(
        default_factory=list,
        metadata={
            "name": "AlternateNumber",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "max_occurs": 32,
        },
    )
