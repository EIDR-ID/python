from app.scheme.org.eidr.schema.asset_doitype import AssetDoitype
from app.scheme.org.eidr.schema.operation_type import OperationType
from app.scheme.org.eidr.schema.alias_type import AliasType
from app.services.registration.interface import RegistrationService


class Alias(RegistrationService):
    """
    Alias operation of the registration service
    """

    name = "register"

    def __init__(self, id: AssetDoitype | str, target_id: AssetDoitype | str):
        self.id = id
        self.target_id = target_id
        super().__init__(id=id, target_id=target_id)

    def validate(self) -> bool:
        if not isinstance(self.id, str):
            raise ValueError("parameter 'id' must be of type str")
        elif not isinstance(self.target_id, str):
            raise ValueError("parameter 'target_id' must be of type str")
        return True

    def objectify(self):
        self.obj = OperationType(
            alias=AliasType(
                id=AssetDoitype(value=self.id),
                target_id=AssetDoitype(value=self.target_id)
            )
        )
