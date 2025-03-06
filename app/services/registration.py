from typing import Union

from app.services.interface import ServiceBase

from app.scheme.org.eidr.schema.request import Request
from app.scheme.org.eidr.schema import OperationType, CreateSeriesDataType, CreateType, CreationType

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
    name = 'register'

    def __init(self, record: Union[CreateSeriesDataType]):
        self.record = record
    def validate(self) -> bool:
        # TODO: add validation logic
        return True

    def objectify(self):
        # TODO: implement logic to match record with asset type (switch case)
        self.obj = Request(operation=[OperationType(create=CreateType(series=self.args.get('record'), type_value=CreationType.CREATE_SERIES))])