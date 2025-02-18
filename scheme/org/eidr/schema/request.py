from dataclasses import dataclass

from scheme.org.eidr.schema.request_type import RequestType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class Request(RequestType):
    class Meta:
        namespace = "http://www.eidr.org/schema"
