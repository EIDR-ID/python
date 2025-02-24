from dataclasses import dataclass

from    .base_asset_doitype import BaseAssetDoitype

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class AssetDoitype(BaseAssetDoitype):
    """
    Restrict assetDOIType to be proper DOIs,and the special bulk ingestion pattern
    see assetDOIType.xsd for this and for localIDType.
    """

    class Meta:
        name = "assetDOIType"
