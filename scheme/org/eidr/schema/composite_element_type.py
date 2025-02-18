from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from scheme.org.eidr.schema.alternate_idtype import AlternateIdtype
from scheme.org.eidr.schema.asset_doitype import AssetDoitype
from scheme.org.eidr.schema.components_mode_type import ComponentsModeType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class CompositeElementType:
    class Meta:
        name = "compositeElementType"

    id: Optional[AssetDoitype] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    other_id: Optional[AlternateIdtype] = field(
        default=None,
        metadata={
            "name": "OtherID",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    source_start: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "SourceStart",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    source_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "SourceDuration",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    components_mode: Optional[ComponentsModeType] = field(
        default=None,
        metadata={
            "name": "ComponentsMode",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    dest_start: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "DestStart",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    dest_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "DestDuration",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "max_length": 128,
        },
    )
