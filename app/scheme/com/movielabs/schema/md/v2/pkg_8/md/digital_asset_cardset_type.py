from dataclasses import dataclass, field
from typing import Optional

from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.string_cardset_type import (
    StringCardsetType,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class DigitalAssetCardsetType:
    """
    EIDR restricts Description to 128 characters.
    """

    class Meta:
        name = "DigitalAssetCardset-type"

    type_value: list[StringCardsetType] = field(
        default_factory=list,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "min_occurs": 1,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "max_length": 128,
        },
    )
    sequence: Optional[int] = field(
        default=None,
        metadata={
            "name": "Sequence",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
