from enum import Enum
from typing import List

from app.scheme.org.eidr.schema.request import Request
from app.scheme.org.eidr.schema.request_type import OperationType
from app.services import Query
from app.services.interface import ServiceBase


class RegistryRequest(ServiceBase):

    # Add any response types into the type below
    response_type: Query.QueryResponseType | Enum | str = None

    def __init__(self, operations: List[ServiceBase]):
        self.response_type = operations[0].response_type
        first = operations[0]
        if isinstance(first, RegistryRequest):
            raise ValueError("Request cannot hold other requests")
        ops = [op.obj for op in operations if isinstance(op, type(first))]
        # Above we ignore anything that doesn't match the first type, and extract the objects
        self.name = operations[0].name
        super().__init__(operations=ops)

    def objectify(self):
        ops: List[OperationType] = self.args.get("operations")
        self.obj = Request(
            operation= ops
        )

    def add(self, other: ServiceBase):
        ops: List[OperationType] = self.args.get("operations")
        if not isinstance(other, type(ops[0])):
            raise ValueError("Batch operations must be of the same type")
    def validate(self) -> bool:
        return True
