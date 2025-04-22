from enum import Enum
from typing import Any, Type

from lxml import etree
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from abc import ABC, abstractmethod

from app.scheme.org.eidr.schema import OperationType, Request




class ServiceBase(ABC):
    serializer = XmlSerializer(config=SerializerConfig(indent="    "))
    ns_map = {"": "http://www.eidr.org/schema"}

    name: str = ""
    xml_name = ""
    is_op: bool = True

    obj: Any = None
    inner_obj: Any = None
    args: dict[str, Any] = dict()
    xml: str = ""
    response_type: Enum | str = ""

    def __init__(self, **kwargs):
        if not self.xml_name:
            self.xml_name = self.name
        self.args = kwargs
        if not self.validate():
            raise ValueError("Service {} could not validate arguments {}".format(type(self).__name__, kwargs))
        self.objectify()
        self.xml = self.serialize()

    @abstractmethod
    def validate(self) -> bool:
        return False

    @abstractmethod
    def objectify(self):
        ...

    def serialize(self) -> str:
        return self.serializer.render(self.obj, self.ns_map)

    def then(self, other: "ServiceBase", token: str):
        if not isinstance(other, type(self)):
            raise ValueError(
                "Service of type {} is not the same type as {}".format(type(other).__name__, type(self).__name__))

        content = {self.xml_name: self.inner_obj, other.xml_name: other.inner_obj
                   }
        inner = [self.inner_obj, other.inner_obj]
        obj = Request(
            operation=inner,
            user_token=token,
        )

        out = Batch(obj)

        return out


class Batch(ServiceBase):
    objects = []

    def __init__(self, obj: Request):
        self.obj = obj
        self.objects = obj.operation

    def validate(self) -> bool:
        """
        Validates the Batch object.

        Returns:
            bool: Always returns True as Batch objects are considered valid by default.
        """
        return True

    def objectify(self):
        """
        Converts the Batch object into its internal representation.
        This method is currently not implemented.
        """
        ...

    def then(self, other: "ServiceBase", token: str | None = None):
        if not isinstance(other, Batch):
            if not isinstance(other, type(self.objects[0])):
                raise ValueError("Batch of type {} is not the same type as Batch of {}".format(type(other).__name__,
                                                                                               type(self).__name__))
            if len(self.objects) >= 10:
                raise ValueError("Batches cannot be larger than 10")
            self.objects.append(other)
            self.obj.operation = self.objects
            self.obj.user_token = token
            return self
        elif isinstance(other.objects[0], type(self.objects[0])):
            if len(self.objects + other.objects) > 10:
                raise ValueError("Batches cannot be larger than 10")
            objects = self.objects + other.objects

            self.obj = Request(operation=objects, user_token=token)
            self.objects = objects
        else:
            raise ValueError("Batch of type {} is not the same type as Batch of {}".format(type(other).__name__,
                                                                                           type(self).__name__))
