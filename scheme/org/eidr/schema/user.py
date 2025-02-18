from dataclasses import dataclass

from scheme.org.eidr.schema.user_resolution_type import UserResolutionType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class User(UserResolutionType):
    class Meta:
        namespace = "http://www.eidr.org/schema"
