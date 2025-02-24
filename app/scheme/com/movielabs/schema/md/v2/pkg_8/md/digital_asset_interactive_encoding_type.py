from dataclasses import dataclass, field
from typing import Optional

from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.string_interactive_enc_runtime_environment import (
    StringInteractiveEncRuntimeEnvironment,
)

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class DigitalAssetInteractiveEncodingType:
    class Meta:
        name = "DigitalAssetInteractiveEncoding-type"

    runtime_environment: Optional[StringInteractiveEncRuntimeEnvironment] = (
        field(
            default=None,
            metadata={
                "name": "RuntimeEnvironment",
                "type": "Element",
                "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
                "required": True,
            },
        )
    )
    first_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "FirstVersion",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "max_length": 64,
        },
    )
    last_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastVersion",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "max_length": 64,
        },
    )
