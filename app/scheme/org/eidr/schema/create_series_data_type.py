from dataclasses import dataclass, field
from typing import Optional

from    .creation_full_info import CreationFullInfo
from    .series_info_type import SeriesInfoType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class CreateSeriesDataType:
    """
    A Series is a root, and can't inherit from anything.
    """

    class Meta:
        name = "createSeriesDataType"

    base_object_data: Optional[CreationFullInfo] = field(
        default=None,
        metadata={
            "name": "BaseObjectData",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    extra_object_metadata: Optional[
        "CreateSeriesDataType.ExtraObjectMetadata"
    ] = field(
        default=None,
        metadata={
            "name": "ExtraObjectMetadata",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )

    @dataclass
    class ExtraObjectMetadata:
        series_info: Optional[SeriesInfoType] = field(
            default=None,
            metadata={
                "name": "SeriesInfo",
                "type": "Element",
                "namespace": "http://www.eidr.org/schema",
                "required": True,
            },
        )
