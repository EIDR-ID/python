from dataclasses import dataclass

from .status_details_type import StatusDetailsType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class AdminResponse(StatusDetailsType):
    class Meta:
        namespace = "http://www.eidr.org/schema"
