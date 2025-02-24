from dataclasses import dataclass, field
from typing import Optional

from    .asset_doitype import AssetDoitype
from    .duplicate_type import DuplicateType
from    .operation_status_details_type import (
    OperationStatusDetailsType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class OperationStatusType:
    """This element type is used to return the status of an operation.

    The elements within this type are (1) Token: the token of the
    operation (2) Status: the status of the operation (3) ID: an
    optional DOI returned only when the request is to create an object.
    The DOI corresponds to the object created (4) Duplicate: Optional,
    but possibly multiple, duplicates are returned when the metadata in
    the request is found not to be unique
    """

    class Meta:
        name = "operationStatusType"

    token: Optional[str] = field(
        default=None,
        metadata={
            "name": "Token",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    status: Optional[OperationStatusDetailsType] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    id: Optional[AssetDoitype] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    duplicate: list[DuplicateType] = field(
        default_factory=list,
        metadata={
            "name": "Duplicate",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
