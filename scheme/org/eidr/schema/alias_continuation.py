from dataclasses import dataclass

from scheme.org.eidr.schema.alias_continuation_type import (
    AliasContinuationType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class AliasContinuation(AliasContinuationType):
    class Meta:
        namespace = "http://www.eidr.org/schema"
