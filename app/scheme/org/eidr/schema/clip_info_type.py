from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from    .asset_doitype import AssetDoitype
from    .components_mode_type import ComponentsModeType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class ClipInfoType:
    """
    A clip can be just an ID, an ID with start and duration, or an ID with just
    duration.
    """

    class Meta:
        name = "clipInfoType"

    parent: Optional[AssetDoitype] = field(
        default=None,
        metadata={
            "name": "Parent",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    components_mode: Optional[ComponentsModeType] = field(
        default=None,
        metadata={
            "name": "ComponentsMode",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    start: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Start",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    duration: list[XmlDuration] = field(
        default_factory=list,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
