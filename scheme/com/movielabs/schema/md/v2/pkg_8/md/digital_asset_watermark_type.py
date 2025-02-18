from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class DigitalAssetWatermarkType:
    """
    Enforce max length on xs:string fields.
    """

    class Meta:
        name = "DigitalAssetWatermark-type"

    vendor: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vendor",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
            "min_length": 2,
            "max_length": 128,
            "pattern": r".*[^\s].*",
        },
    )
    product_and_version_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProductAndVersionID",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
            "max_length": 128,
        },
    )
    data: Optional[str] = field(
        default=None,
        metadata={
            "name": "Data",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
            "required": True,
            "max_length": 256,
        },
    )
    guaranteed_absent: Optional[bool] = field(
        default=None,
        metadata={
            "name": "guaranteedAbsent",
            "type": "Attribute",
        },
    )
