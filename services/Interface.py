from typing import Any

from lxml import etree
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from abc import ABC, abstractmethod


class ServiceBase(ABC):
    serializer = XmlSerializer(config=SerializerConfig(indent="    "))
    ns_map = {"": "http://www.eidr.org/schema"}

    name: str = ""

    obj: Any = None
    args: dict[str, Any] = dict()
    xml: str = ""

    def __init__(self, **kwargs):
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
