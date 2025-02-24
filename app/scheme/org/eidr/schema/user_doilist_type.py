from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class UserDoilistType:
    class Meta:
        name = "userDOIListType"

    user_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "UserID",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "pattern": r"10\.5238/[0-9a-zA-Z_#\.\-\(\)]{3,32}",
        },
    )
