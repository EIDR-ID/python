from app.scheme.org.eidr.schema import OperationType
from app.services.interface import ServiceBase
from app.scheme.org.eidr.schema.delete_type import DeleteType
from app.scheme.org.eidr.schema.asset_doitype import AssetDoitype

class Delete(ServiceBase):
    name = "register"

    def __init__(self, id: str):
        super().__init__(id=id)

    def validate(self) -> bool:
        expected = {
            "id": str
        }

        for arg, arg_type in expected.items():
            if arg in self.args:
                if not isinstance(self.args[arg], arg_type):
                    raise ValueError(
                        "Arg {} is of type {}, must be a {}".format(arg, type(self.args[arg]).__name__,
                                                                    arg_type.__name__))

        return True

    def objectify(self):
        id: str = self.args.get("id")
        self.obj = OperationType(
            delete=DeleteType(
            id= AssetDoitype(value=id)
        ))

