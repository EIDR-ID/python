from dataclasses import dataclass

from scheme.org.eidr.schema.asset_doilist_type import AssetDoilistType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class AssetIdlist(AssetDoilistType):
    class Meta:
        name = "AssetIDList"
        namespace = "http://www.eidr.org/schema"
