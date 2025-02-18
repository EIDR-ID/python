from dataclasses import dataclass, field
from typing import Optional

from scheme.org.doi.pkg_2010.doischema.kernel_metadata import KernelMetadata
from scheme.org.eidr.schema.all_inherited_info_type import AllInheritedInfoType
from scheme.org.eidr.schema.all_self_defined_info_type import (
    AllSelfDefinedInfoType,
)
from scheme.org.eidr.schema.full_object_info_type import FullObjectInfoType
from scheme.org.eidr.schema.provenance_info_type import ProvenanceInfoType
from scheme.org.eidr.schema.resolution_type_type import ResolutionTypeType
from scheme.org.eidr.schema.simple_info_type import SimpleInfoType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class ResolutionSetType:
    """This is used by the SDK and atomic tools to return a set of resolutions as a
    valid piece of XML; the Registry only supports doing resolutions one at a time,
    and all of the results are put in a Resolutions element of this type.

    Most of the tools will generate only a single kind of Resolution at
    a time.  As of 1.2.1, GraphTool and ResolveTool are the only
    exceptions to this. If the "singleType" attribute is present, it
    contains the name of the single type of resolution contained by
    <Resolutions xmlns=""/>
    """

    class Meta:
        name = "resolutionSetType"

    simple_metadata: list[SimpleInfoType] = field(
        default_factory=list,
        metadata={
            "name": "SimpleMetadata",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    self_defined_metadata: list[AllSelfDefinedInfoType] = field(
        default_factory=list,
        metadata={
            "name": "SelfDefinedMetadata",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    inherited_metadata: list[AllInheritedInfoType] = field(
        default_factory=list,
        metadata={
            "name": "InheritedMetadata",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    full_metadata: list[FullObjectInfoType] = field(
        default_factory=list,
        metadata={
            "name": "FullMetadata",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    provenance_metadata: list[ProvenanceInfoType] = field(
        default_factory=list,
        metadata={
            "name": "ProvenanceMetadata",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    kernel_metadata: list[KernelMetadata] = field(
        default_factory=list,
        metadata={
            "name": "kernelMetadata",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    single_type: Optional[ResolutionTypeType] = field(
        default=None,
        metadata={
            "name": "singleType",
            "type": "Attribute",
        },
    )
