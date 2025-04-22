from abc import ABC

from app.services import ServiceBase


"""
    Base class for no-operation requests in the EIDR API.

    This class serves as a base for requests that do not belong in an
    operation. See EDIR API documentation for more details.
"""
class NoOperationRequest(ServiceBase, ABC):
    is_op = False
    ...