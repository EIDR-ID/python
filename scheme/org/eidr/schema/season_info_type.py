from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDate, XmlPeriod

from scheme.org.eidr.schema.asset_doitype import AssetDoitype
from scheme.org.eidr.schema.season_class_type import SeasonClassType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class SeasonInfoType:
    """Season must supply base object ReferentType, StructuralType, and
    ReleaseDate.

    baseObjectData.ApproximateLength must be 0 (zero) the typical length
    of an episode. baseObjectData.ResourceName is used to provide a
    season title and is required, but may be submitted empty or replaced
    with a system-generated name under special circumstances.
    """

    class Meta:
        name = "seasonInfoType"

    parent: Optional[AssetDoitype] = field(
        default=None,
        metadata={
            "name": "Parent",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    end_date: Optional[Union[XmlPeriod, XmlDate]] = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    season_class: list[SeasonClassType] = field(
        default_factory=list,
        metadata={
            "name": "SeasonClass",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    number_required: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NumberRequired",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    date_required: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DateRequired",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    original_title_required: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OriginalTitleRequired",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    sequence_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "SequenceNumber",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
