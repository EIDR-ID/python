from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class DigitalAssetAudioMcalabelType:
    class Meta:
        name = "DigitalAssetAudioMCALabel-type"

    content_kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContentKind",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    element_kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "ElementKind",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
