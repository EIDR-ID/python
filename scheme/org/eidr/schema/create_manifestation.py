from dataclasses import dataclass

from scheme.org.eidr.schema.create_manifestation_data_type import (
    CreateManifestationDataType,
)

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class CreateManifestation(CreateManifestationDataType):
    class Meta:
        namespace = "http://www.eidr.org/schema"
