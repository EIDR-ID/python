from typing import Union

from app.services import ServiceBase
from app.scheme.org.eidr.schema import OperationType, TargetRelationshipType, AssetDoitype, RemoveRelationshipType

class RemoveRelationship(ServiceBase):
    name = "register"

    def __init__(self, id: Union[AssetDoitype,str], target_id: Union[AssetDoitype,str], type_value: TargetRelationshipType):
        self.id = id
        self.target_id = target_id
        self.type_value = type_value
        super().__init__()

    def validate(self) -> bool:
        if not isinstance(self.id, (str, AssetDoitype)):
            raise ValueError("ID must be a string or AssetDoitype")
        if not isinstance(self.target_id, (str, AssetDoitype)):
            raise ValueError(f"Target ID must be a string or {type(self.target_id)}")
        if not isinstance(self.type_value, TargetRelationshipType):
            raise ValueError(f"Type value must be an instance of {type(self.type_value)}")
        return True

    def objectify(self):
        self.obj = OperationType(
            remove_relationship= RemoveRelationshipType(
                id=AssetDoitype(value=self.id) if isinstance(self.id, str) else self.id,
                target_id=AssetDoitype(value=self.target_id) if isinstance(self.target_id, str) else self.target_id,
                type_value=self.type_value,
            )
        )
