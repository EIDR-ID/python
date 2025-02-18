from dataclasses import dataclass, field
from typing import Optional

from scheme.com.movielabs.schema.md.v2.pkg_8.md.comp_obj_type import (
    CompObjType,
)
from scheme.org.eidr.schema.creation_full_info import CreationFullInfo

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class CreateCompilationDataType:
    """
    A Compilation is a root, and can't inherit from anything.
    """

    class Meta:
        name = "createCompilationDataType"

    base_object_data: Optional[CreationFullInfo] = field(
        default=None,
        metadata={
            "name": "BaseObjectData",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    extra_object_metadata: Optional[
        "CreateCompilationDataType.ExtraObjectMetadata"
    ] = field(
        default=None,
        metadata={
            "name": "ExtraObjectMetadata",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )

    @dataclass
    class ExtraObjectMetadata:
        compilation_info: Optional[CompObjType] = field(
            default=None,
            metadata={
                "name": "CompilationInfo",
                "type": "Element",
                "namespace": "http://www.eidr.org/schema",
                "required": True,
            },
        )
