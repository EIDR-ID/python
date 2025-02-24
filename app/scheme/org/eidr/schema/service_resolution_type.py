from dataclasses import dataclass, field
from typing import Optional

from    .alt_service_name_type import AltServiceNameType
from    .delivery_model_type import DeliveryModelType
from    .service_alternate_id_type import (
    ServiceAlternateIdType,
)
from    .service_name_type import ServiceNameType
from    .time_zone_type import TimeZoneType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class ServiceResolutionType:
    """
    Returned when resolving a service; Used when modifying a service.
    """

    class Meta:
        name = "serviceResolutionType"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
            "pattern": r"10\.5239/[\dA-F]{4}-[\dA-F]{4}",
        },
    )
    service_name: Optional[ServiceNameType] = field(
        default=None,
        metadata={
            "name": "ServiceName",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    alternate_service_name: list[AltServiceNameType] = field(
        default_factory=list,
        metadata={
            "name": "AlternateServiceName",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "max_occurs": 10,
        },
    )
    alternate_id: list[ServiceAlternateIdType] = field(
        default_factory=list,
        metadata={
            "name": "AlternateID",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "max_occurs": 10,
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
    parent: Optional[str] = field(
        default=None,
        metadata={
            "name": "Parent",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "pattern": r"10\.5239/[\dA-F]{4}-[\dA-F]{4}",
        },
    )
    other_affiliation: list[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherAffiliation",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "max_occurs": 10,
            "pattern": r"10\.5239/[\dA-F]{4}-[\dA-F]{4}",
        },
    )
    active: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Active",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    primary_time_zone: Optional[TimeZoneType] = field(
        default=None,
        metadata={
            "name": "PrimaryTimeZone",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    region: Optional[str] = field(
        default=None,
        metadata={
            "name": "Region",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "max_length": 128,
        },
    )
    primary_audio_language: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrimaryAudioLanguage",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    delivery_model: list[DeliveryModelType] = field(
        default_factory=list,
        metadata={
            "name": "DeliveryModel",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "max_occurs": 4,
        },
    )
