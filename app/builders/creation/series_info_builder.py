from .helpers import get_enum

from typing import Union, Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from app.scheme.org.eidr.schema.series_info_type import SeriesInfoType
from app.scheme.org.eidr.schema.series_class_type import SeriesClassType

class SeriesInfoBuilder:
    """
    Extra Object MetaData Builder for a Series record
    """

    def __init__(self):
        self.end_date: Optional[Union[XmlDate, XmlDateTime]] = None
        self.number_required: Optional[bool] = None
        self.date_required: Optional[bool] = None
        self.original_title_required: Optional[bool] = None
        self.series_class: Optional[SeriesClassType] = None
    def build(self) -> SeriesInfoType:
        return SeriesInfoType(
            end_date=self.end_date,
            series_class=self.series_class,
            number_required=self.number_required,
            date_required=self.date_required,
            original_title_required=self.original_title_required,
        )

    def set_end_date(self, end_date: str):
        """
        set the end date of the record
        :param end_date the end date of the record Format "YYYY-MM-DD"
        """
        self.end_date = XmlDate.from_string(end_date)
        return self

    def set_series_class(self, series_class: str):
        """
        Set the series class of the record
        :param series_class: the series class of the record
        """
        self.series_class = get_enum(
            enum_class=SeriesClassType,
            enum_value=series_class
        ) if series_class is not None else None
        return self

    def set_number_required(self, number_required: bool):
        """
        Set the number required field
        :param number_required: bool
        """
        self.number_required = number_required
        return self

    def set_date_required(self, date_required: bool):
        """
        Set the date required field
        param date_required: bool
        """
        self.date_required = date_required
        return self

    def set_original_title_required(self, original_title_required: bool):
        """
        Set the original title required field
        original_title_required: bool
        """
        self.original_title_required = original_title_required
        return self