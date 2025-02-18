from dataclasses import dataclass

from scheme.org.eidr.schema.user_creation_type import UserCreationType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class CreateUser(UserCreationType):
    class Meta:
        namespace = "http://www.eidr.org/schema"
