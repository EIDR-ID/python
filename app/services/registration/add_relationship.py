
from app.scheme.org.eidr.schema.add_relationship_type import AddRelationshipType
from app.services.registration.interface import RegistrationService
from app.services import ServiceBase
from app.scheme.org.eidr.schema import OperationType, AddRelationshipType


class AddRelationship(RegistrationService):
    """
    This class represents the add relationship operation request within the registration service.
        Attributes:
            relationship: The relationship to be added (AddRelationshipType)
    """
    name = "register"

    def __init__(self, relationship: AddRelationshipType):
        self.relationship = relationship
        super().__init__()

    def validate(self) -> bool:
        tp = type(AddRelationshipType())
        if not isinstance(self.relationship, tp):
            raise TypeError(f"'Relationship' obj is of type {type(self.relationship)} "
                            f"should be of type {type(tp)}")
        return True

    def objectify(self):
        self.obj = OperationType(
            add_relationship=self.relationship
        )
