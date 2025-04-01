from typing import Optional, TypedDict, Union

from xsdata.models.datatype import XmlDuration

from app.scheme.org.eidr.schema import CompositeClassType
from app.scheme.org.eidr.schema.alternate_idtype import AlternateIdtype
from app.scheme.org.eidr.schema.composite_element_type import CompositeElementType
from app.scheme.org.eidr.schema.asset_doitype import AssetDoitype
from app.scheme.org.eidr.schema.composite_info_type import CompositeInfoType
from app.scheme.org.eidr.schema.promotion_info_type import PromotionInfoType
from app.scheme.org.eidr.schema.supplemental_content_info_type import SupplementalContentInfoType
from app.scheme.org.eidr.schema.alternate_content_info_type import AlternateContentInfoType
from app.scheme.org.eidr.schema.packaging_info_type import PackagingInfoType
from app.scheme.org.eidr.schema.components_mode_type import ComponentsModeType
from app.scheme.org.eidr.schema.target_relationship_type import TargetRelationshipType
from app.builders.creation.helpers import get_enum
from app.scheme.org.eidr.schema.add_relationship_type import AddRelationshipType


class CompositeElementTypeDict(TypedDict):
    """
    TypedDict for CompositeElementType
    """
    id: Optional[str]
    other_id: Optional[AlternateIdtype]
    source_start: Optional[XmlDuration]
    source_duration: Optional[XmlDuration]
    components_mode: Optional[ComponentsModeType]
    dest_start: Optional[XmlDuration]
    dest_duration: Optional[XmlDuration]
    description: Optional[str]


class AddRelationShipTypeBuilder:
    """
    Builder for AddRelationshipType

    Attributes:
        id: AssetDoitype
        composite_info: CompositeInfoType
        promotion_info: PromotionInfoType
        supplemental_content_info: SupplementalContentInfoType
        alternate_content_info: AlternateContentInfoType
        packing_info: PackagingInfoType
        type_value: TargetRelationshipType
    """
    def __init__(self):
        self.id: AssetDoitype
        self.composite_info: Optional[CompositeInfoType] = None
        self.promotion_info: Optional[PromotionInfoType] = None
        self.supplemental_content_info: Optional[SupplementalContentInfoType] = None
        self.alternate_content_info: Optional[AlternateContentInfoType] = None
        self.packing_info: Optional[PackagingInfoType] = None
        self.type_value: TargetRelationshipType

    def build(self):
        return AddRelationshipType(
            id=self.id,
            composite_info=self.composite_info,
            promotion_info=self.promotion_info,
            supplemental_content_info=self.supplemental_content_info,
            alternate_content_info=self.alternate_content_info,
            packaging_info=self.packing_info,
            type_value=self.type_value
        )

    def set_id(self, id: Optional[Union[AssetDoitype, str]]):
        """
        Set the ID of the record that will receive the relationship.
        :param id: EIDR ID
        :return: self
        """
        if isinstance(id, str):
            self.id = AssetDoitype(id)
        elif isinstance(id, AssetDoitype):
            self.id = id
        else:
            raise ValueError("'id' must be a string or AssetDoitype")
        return self

    def set_composite_info(
            self,
            composite_class: Optional[CompositeClassType],
            element: Optional[list[CompositeElementTypeDict]] = None,
    ):
        """
        Set the composite info of this relationship.
        :param composite_class: the composite class
        :param element: list of CompositeElementTypeDict
        :return: self
        """
        self.composite_info = CompositeInfoType(
            composite_class=get_enum(CompositeClassType, composite_class),
            element=[
                CompositeElementType(
                    id=e.get("id"),
                    other_id=e.get("other_id"),
                    source_start=e.get("source_start"),
                    source_duration=e.get("source_duration"),
                    components_mode=e.get("components_mode"),
                    dest_start=e.get("dest_start"),
                    dest_duration=e.get("dest_duration"),
                    description=e.get("description")
                ) for e in element
            ]
        )
        return self

    def set_promotion_info(
            self,
            id: Union[AssetDoitype, str],
            promotion_class: Optional[Union[str, PromotionInfoType]],
    ):
        """
        Set the promotion info of this relationship.
        :param id: EIDR ID
        :param promotion_class: the promotion class
        :return: self
        """
        if isinstance(id, str):
            id = AssetDoitype(id)
        elif not isinstance(id, AssetDoitype):
            raise ValueError("'id' must be a string or AssetDoitype")
        self.promotion_info = PromotionInfoType(
            id=id,
            promotion_class=get_enum(PromotionInfoType, promotion_class)
        )
        return self

    def set_supplemental_content_info(self,
                                      id: Union[AssetDoitype, str],
                                      supplemental_class: Optional[str],
                                      ):
        """
        Set the supplemental content info of this relationship.
        :param id: EIDR ID
        :param supplemental_class: the supplemental class
        :return: self
        """
        if isinstance(id, str):
            id = AssetDoitype(id)
        elif not isinstance(id, AssetDoitype):
            raise ValueError("'id' must be a string or AssetDoitype")
        self.supplemental_content_info = SupplementalContentInfoType(
            id=id,
            supplemental_content_class=get_enum(SupplementalContentInfoType, supplemental_class)
        )
        return self

    def set_alternate_content_info(
            self,
            id: Union[AssetDoitype, str],
            alternate_class: Optional[str],
    ):
        """
        Set the alternate content info of this relationship.
        :param id: EIDR ID
        :param alternate_class: the alternate class
        :return: self
        """
        if isinstance(id, str):
            id = AssetDoitype(id)
        elif not isinstance(id, AssetDoitype):
            raise ValueError("'id' must be a string or AssetDoitype")
        self.alternate_content_info = AlternateContentInfoType(
            id=id,
            alternate_content_class=get_enum(AlternateContentInfoType, alternate_class)
        )
        return self

    def set_packaging_info(
            self,
            id: Union[AssetDoitype, str],
            packaging_class: Optional[str],
    ):
        """
        Set the packaging info of this relationship.
        :param id: EIDR ID
        :param packaging_class: the packaging class
        :return: self
        """
        if isinstance(id, str):
            id = AssetDoitype(id)
        elif not isinstance(id, AssetDoitype):
            raise ValueError("'id' must be a string or AssetDoitype")
        self.packing_info = PackagingInfoType(
            id=id,
            packaging_class=get_enum(PackagingInfoType, packaging_class)
        )
        return self

    def set_type_value(self, type_value: Optional[Union[str, TargetRelationshipType]]):
        """
        Set the type value of this relationship:

        - "CompositeRelationship"
        - "PackagingRelationship"
        - "SupplementalRelationship"
        - "PromotionalRelationship"
        - "AlternateContentRelationship"
        :param type_value: the type value
        :return: self
        """
        self.type_value = get_enum(TargetRelationshipType, type_value)
        return self
