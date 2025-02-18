from enum import Enum

__NAMESPACE__ = "http://www.eidr.org/schema"


class DeliveryModelType(Enum):
    LINEAR = "Linear"
    VOD = "VOD"
    OTHER = "Other"
