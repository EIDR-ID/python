from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class MetadataAuthorityType:
    class Meta:
        name = "metadataAuthorityType"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"10\.5237/[0-9a-fA-F]{4}-[0-9a-fA-F]{4}|10\.5237/superparty",
        },
    )
