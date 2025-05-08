from app.services.registration.interface import RegistrationService



class Promote(RegistrationService):
    """
    This class represents the promote operation within the registration service.
    Promote operation updates the status field of a record from "in development" to "valid"
    """

    def validate(self) -> bool:
        if not self.args:
            return False
        elif not isinstance(self.args.get("id"), str):
            id = self.args.get("id")
            raise TypeError(f"Expected 'id' to be of type str, but got {type(id)}")
        return True

    def objectify(self):
        self.obj = OperationType(
            promote=PromoteType(
                id=AssetDoitype(self.args.get("id"))
            )
        )
