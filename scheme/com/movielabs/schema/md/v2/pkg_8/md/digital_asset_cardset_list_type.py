from dataclasses import dataclass, field

from scheme.com.movielabs.schema.md.v2.pkg_8.md.digital_asset_cardset_type import (
    DigitalAssetCardsetType,
)
from scheme.com.movielabs.schema.md.v2.pkg_8.md.made_for_region_type import (
    MadeForRegionType,
)
from scheme.com.movielabs.schema.md.v2.pkg_8.md.string_cardset_list_type import (
    StringCardsetListType,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class DigitalAssetCardsetListType:
    class Meta:
        name = "DigitalAssetCardsetList-type"

    type_value: list[StringCardsetListType] = field(
        default_factory=list,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    region: list[MadeForRegionType] = field(
        default_factory=list,
        metadata={
            "name": "Region",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    cardset: list[DigitalAssetCardsetType] = field(
        default_factory=list,
        metadata={
            "name": "Cardset",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "min_occurs": 1,
        },
    )
