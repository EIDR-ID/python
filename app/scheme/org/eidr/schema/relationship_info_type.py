from dataclasses import dataclass, field
from typing import Optional

from    .asset_doitype import AssetDoitype
from    .relationship_type import RelationshipType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class RelationshipInfoType(AssetDoitype):
    """a relationship is described with "<Relationship xmlns="" type="{http://www.eidr.org/schema}isSeasonOf">assetDOI</Relationship>" isCompositeOf and isCompilation
    of can occur multiple times in a relationship list (see SimpleMetadata), once for
    each item in the composite. The lightweight relationships ca occur multiple times.
    Other relationships occur once on any given object."""

    class Meta:
        name = "relationshipInfoType"

    type_value: Optional[RelationshipType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )
