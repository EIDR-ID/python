from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDate, XmlPeriod

from scheme.org.eidr.schema.series_class_type import SeriesClassType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class SeriesInfoType:
    """Series must supply base object ReferentType, StructuralType,
    OriginalLanguage, and ReleaseDate.

    baseObjectData.ApproximateLength must be 0 (zero) or the typical
    length of an episode
    """

    class Meta:
        name = "seriesInfoType"

    end_date: Optional[Union[XmlPeriod, XmlDate]] = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    series_class: Optional[SeriesClassType] = field(
        default=None,
        metadata={
            "name": "SeriesClass",
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
