from app.services import ServiceBase

from app.scheme.org.eidr.schema.add_relationship_type import AddRelationshipType

class AddRelationship(ServiceBase):

    name = "register"

    def __init__(self, relationship: AddRelationshipType):
        self.relationship = relationship
        super().__init__()

    def validate(self) -> bool:
        if isinstance(self.relationship, AddRelationship):
            return False
        return True

    def objectify(self):
        self.obj = self.relationship
