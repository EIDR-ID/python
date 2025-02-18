from dataclasses import dataclass

from scheme.org.eidr.schema.response_type import ResponseType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class Response(ResponseType):
    class Meta:
        namespace = "http://www.eidr.org/schema"
