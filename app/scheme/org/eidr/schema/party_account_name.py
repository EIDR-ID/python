from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class PartyAccountName:
    class Meta:
        namespace = "http://www.eidr.org/schema"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[0-9a-zA-Z_# \.\-\(\)]{2,64}",
        },
    )
