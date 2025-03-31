from abc import ABC

from app.services import ServiceBase


class NoOperationRequest(ServiceBase, ABC):
    is_op = False
    ...