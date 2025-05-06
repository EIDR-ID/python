from abc import ABC

from app.services import ServiceBase
from typing import Generic, TypeVar

T = TypeVar('T', bound=ServiceBase)

"""
    Base class for no-operation requests in the EIDR API.

    This class serves as a base for requests that do not belong in an
    operation. See EDIR API documentation for more details.
"""


class NoOperationRequest(Generic[T], ServiceBase, ABC):
    is_op = False
    response_type: str | None = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if hasattr(self.obj, "response_type"):
            self.response_type = self.obj.response_type
