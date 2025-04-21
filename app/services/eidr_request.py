from enum import Enum
from typing import List

from app.scheme.org.eidr.schema.request import Request
from app.scheme.org.eidr.schema.request_type import OperationType
from app.services import Query
from app.services.interface import ServiceBase


class RegistryRequest(ServiceBase):
    """
    A class representing a registry request.

    Attributes:
        response_type (Query.QueryResponseType | Enum | str): The type of response expected from the request.

    Methods:
        __init__(operations: List[ServiceBase]):
            Initializes the RegistryRequest with a list of operations.
        objectify():
            Converts the operations into a Request object.
        add(other: ServiceBase):
            Adds another operation to the batch, ensuring it is of the same type.
        validate() -> bool:
            Validates the request.
    """

    # Add any response types into the type below
    response_type: Query.QueryResponseType | Enum | str = None

    def __init__(self, operations: List[ServiceBase]):
        """
        Initializes the RegistryRequest with a list of operations.

        Parameters:
            operations (List[ServiceBase]): A list of ServiceBase operations.

        Raises:
            ValueError: If the first operation is a RegistryRequest or if operations are of mixed types.
        """
        self.response_type = operations[0].response_type
        first = operations[0]
        if isinstance(first, RegistryRequest):
            raise ValueError("Request cannot hold other requests")
        ops = [op.obj for op in operations if isinstance(op, type(first))]
        # Above we ignore anything that doesn't match the first type, and extract the objects
        self.name = operations[0].name
        super().__init__(operations=ops)

    def objectify(self):
        """
        Converts the operations into a Request object.
        """
        ops: List[OperationType] = self.args.get("operations")
        self.obj = Request(
            operation=ops
        )

    def add(self, other: ServiceBase):
        """
        Adds another operation to the batch.

        Parameters:
            other (ServiceBase): The operation to add.

        Raises:
            ValueError: If the operation type does not match the existing batch type.
        """
        ops: List[OperationType] = self.args.get("operations")
        if not isinstance(other, type(ops[0])):
            raise ValueError("Batch operations must be of the same type")

    def validate(self) -> bool:
        """
        Validates the request.

        Returns:
            bool: Always returns True.
        """
        return True