from app.services.interface import ServiceBase

from app.scheme.org.eidr.schema.request import Request
from app.scheme.org.eidr.schema import OperationType

"""
This service provides the following content operations:
    - Create Object
    - Add Relationship
    - Remove Relationship
    - Replace Relationship
    - Modify
    - Delete
    - Alias
    - Promote
"""

class Registration(ServiceBase):
    name = 'registration'

    def validate(self) -> bool:
        pass

    def objectify(self):
        self.obj = Request(operation=[OperationType()])