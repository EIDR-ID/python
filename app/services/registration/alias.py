from app.scheme.org.eidr.schema.asset_doitype import AssetDoitype
from app.scheme.org.eidr.schema.operation_type import OperationType
from app.scheme.org.eidr.schema.alias_type import AliasType
from app.services import ServiceBase


class Alias (ServiceBase):
    """
    Alias operation of the registration service
    """

    name = "register"

    def __init__(self, id:AssetDoitype, target_id:AssetDoitype):
        self.id = id
        self.target_id = target_id
        super().__init__(id=id, target_id=target_id)

    def validate(self) -> bool:
        if not isinstance(self.id, AssetDoitype):
            raise ValueError("'id' must be an instance of AssetDoitype")
        elif not isinstance(self.target_id, AssetDoitype):
            raise ValueError("'target_id' must be an instance of AssetDoitype")
        return True

    def objectify(self):
        self.obj = OperationType(
            alias=AliasType(
                id=self.id,
                target_id=self.target_id
            )
        )
