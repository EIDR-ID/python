from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from scheme.org.eidr.schema.administrators_info_type import (
    AdministratorsInfoType,
)
from scheme.org.eidr.schema.asset_doitype import AssetDoitype
from scheme.org.eidr.schema.status_type import StatusType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class ProvenanceInfoType:
    """
    Returned by provenance resolution.
    """

    class Meta:
        name = "provenanceInfoType"

    id: Optional[AssetDoitype] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    issue_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "IssueNumber",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    status: Optional[StatusType] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    administrators: Optional[AdministratorsInfoType] = field(
        default=None,
        metadata={
            "name": "Administrators",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    created_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "CreatedBy",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "pattern": r"10\.5238/[0-9a-zA-Z_#\.\-\(\)]{3,32}",
        },
    )
    creation_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreationDate",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    last_modified_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastModifiedBy",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "pattern": r"10\.5238/[0-9a-zA-Z_#\.\-\(\)]{3,32}",
        },
    )
    last_modification_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LastModificationDate",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    publication_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "PublicationDate",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
