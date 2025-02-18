from dataclasses import dataclass, field
from typing import Optional

from scheme.org.eidr.schema.failed_dependency_type import FailedDependencyType
from scheme.org.eidr.schema.operation_status_type import OperationStatusType
from scheme.org.eidr.schema.ready_to_submit_type import ReadyToSubmitType
from scheme.org.eidr.schema.waiting_on_dependencies_type import (
    WaitingOnDependenciesType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class BulkItemInfoType:
    """For file status of Processing and Done, each item has one of the following
    as status:

    --Waiting on dependencies: list of dependencies that have ot be resolvedbefore this item can be registered
    --Ready to submit: all dependencies are cleared, and the item can be submitted
    --Success: object registered successfully, and a DOI is returned
    --Failed (duplicate): an identical object already exists. a single duplicate is a valid replacement for the object's localID in
    dependent items in the bulk file, but multiple duplicates are a real failure. the DOIs are in the one or more Duplicate fields in this element
    --Failed (other): returns status/error information from the registry
    --Failed (dependency: one of the objects on which the item depends failed to register. list on or more localIDs of failed items on which
    there is a dependency
    --Pending: details returned by Registry with this state, including the transaction token, which other applications can
    use (if they have the appropriate permissions.)
    --Rejected: object was rejected due to incorrect or insufficient metadata.
    """

    class Meta:
        name = "bulkItemInfoType"

    waiting: Optional[WaitingOnDependenciesType] = field(
        default=None,
        metadata={
            "name": "Waiting",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    ready: Optional[ReadyToSubmitType] = field(
        default=None,
        metadata={
            "name": "Ready",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    success: Optional[OperationStatusType] = field(
        default=None,
        metadata={
            "name": "Success",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    failed_duplicate: Optional[OperationStatusType] = field(
        default=None,
        metadata={
            "name": "FailedDuplicate",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    failed_other: Optional[OperationStatusType] = field(
        default=None,
        metadata={
            "name": "FailedOther",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    failed_dependency: Optional[FailedDependencyType] = field(
        default=None,
        metadata={
            "name": "FailedDependency",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    pending: Optional[OperationStatusType] = field(
        default=None,
        metadata={
            "name": "Pending",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    rejected: Optional[OperationStatusType] = field(
        default=None,
        metadata={
            "name": "Rejected",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
