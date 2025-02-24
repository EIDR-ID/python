from dataclasses import dataclass

from    .user_doilist_type import UserDoilistType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class UserIdlist(UserDoilistType):
    class Meta:
        name = "UserIDList"
        namespace = "http://www.eidr.org/schema"
