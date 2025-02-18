from dataclasses import dataclass, field

from scheme.org.eidr.schema.asset_doitype import AssetDoitype

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class AssetDoilistType:
    class Meta:
        name = "assetDOIListType"

    asset_id: list[AssetDoitype] = field(
        default_factory=list,
        metadata={
            "name": "AssetID",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
