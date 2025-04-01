from typing import Optional

from app.builders.creation.base_object_builder_exception import BaseObjectException
from app.scheme.com.movielabs.schema.md.v2.pkg_8.md.string_interactive_type import StringInteractiveType
from app.scheme.com.movielabs.schema.md.v2.pkg_8.md.string_interactive_format_type import  StringInteractiveFormatType
from app.scheme.com.movielabs.schema.md.v2.pkg_8.md.digital_asset_interactive_base_data_type import DigitalAssetInteractiveBaseDataType
from app.builders.creation.helpers import get_enum

class DigitalAssetInteractiveBaseDataBuilder:
    def __init__(self):
        self.type_value: Optional[StringInteractiveType] = None
        self.format_type: Optional[StringInteractiveFormatType] = None
        self.lang: Optional[str] = None

    def build(self) -> DigitalAssetInteractiveBaseDataType:
        if self.type_value is None:
            raise BaseObjectException("field 'type value' is required")
        return DigitalAssetInteractiveBaseDataType(
            type_value=self.type_value,
            format_type= self.format_type,
            language=self.lang
        )

    def set_type_value(self, type_value:Optional[StringInteractiveType,str]):
        """
        Set the type value of this interactive record:

        - "360"
        - "AR"
        - "Comic"
        - "Commerce"
        - "Image"
        - "Interactivity"
        - "Live"
        - "Location"
        - "MR"
        - "Menu"
        - "Mixed-Media"
        - "Overlay Game"
        - "Skins"
        - "Standalone Game"
        - "VR"
        - "Other"
        :param type_value: the type_value of this interactive record
        :return: self
        """
        try:
            get_enum(StringInteractiveType, type_value)
        except ValueError as e:
            raise e
        return self

    def set_format_type(self, format_type:Optional[StringInteractiveFormatType,str]):
        """
        Set the format type of this interactive record:

        - "Text"
        - "Executable"
        - "Metadata"
        :param format_type: the format type
        :return: self
        """

        try:
            self.format_type = get_enum(StringInteractiveFormatType, format_type)
        except ValueError as e:
            raise e
        return self

