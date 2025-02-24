from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class LanguagesType:
    class Meta:
        name = "languagesType"

    language: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "min_occurs": 1,
        },
    )
