from abc import ABC

from app.services import ServiceBase


class RegistrationService(ServiceBase, ABC):
    name = "register"
