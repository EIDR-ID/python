from dataclasses import dataclass, field
from typing import Optional, Union

from    .alternate_content_class_type import (
    AlternateContentClassType,
)
from    .asset_doitype import AssetDoitype
from    .create_clip_data_type import CreateClipDataType
from    .create_compilation_data_type import (
    CreateCompilationDataType,
)
from    .create_edit_data_type import CreateEditDataType
from    .create_episode_data_type import (
    CreateEpisodeDataType,
)
from    .create_interactive_data_type import (
    CreateInteractiveDataType,
)
from    .create_manifestation_data_type import (
    CreateManifestationDataType,
)
from    .create_season_data_type import CreateSeasonDataType
from    .create_series_data_type import CreateSeriesDataType
from    .modify_basic_data_type import ModifyBasicDataType
from    .modify_composite_data_type import (
    ModifyCompositeDataType,
)
from    .packaging_class_type import PackagingClassType
from    .promotion_class_type import PromotionClassType
from    .query_results_type import QueryResultsType
from    .query_type import QueryType
from    .report_query_type import ReportQueryType
from    .report_results_type import ReportResultsType
from    .request_status_results_type import (
    RequestStatusResultsType,
)
from    .request_status_type import RequestStatusType
from    .series_ancestry_type import SeriesAncestryType
from    .simple_info_type import SimpleInfoType
from    .status_details_type import StatusDetailsType
from    .supplemental_content_class_type import (
    SupplementalContentClassType,
)
from    .target_relationship_type import (
    TargetRelationshipType,
)
from    .token_cancellation_results_type import (
    TokenCancellationResultsType,
)
from    .virtual_fields_type import VirtualFieldsType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class ResponseType:
    class Meta:
        name = "responseType"

    status: Optional[StatusDetailsType] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "required": True,
        },
    )
    request_status: Optional[RequestStatusType] = field(
        default=None,
        metadata={
            "name": "RequestStatus",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    request_status_results: Optional[RequestStatusResultsType] = field(
        default=None,
        metadata={
            "name": "RequestStatusResults",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    token_cancellation_results: Optional[TokenCancellationResultsType] = field(
        default=None,
        metadata={
            "name": "TokenCancellationResults",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    basic: Optional[ModifyBasicDataType] = field(
        default=None,
        metadata={
            "name": "Basic",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    series: Optional[CreateSeriesDataType] = field(
        default=None,
        metadata={
            "name": "Series",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    interactive: Optional[CreateInteractiveDataType] = field(
        default=None,
        metadata={
            "name": "Interactive",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    season: Optional[CreateSeasonDataType] = field(
        default=None,
        metadata={
            "name": "Season",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    episode: Optional[CreateEpisodeDataType] = field(
        default=None,
        metadata={
            "name": "Episode",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    manifestation: Optional[CreateManifestationDataType] = field(
        default=None,
        metadata={
            "name": "Manifestation",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    edit: Optional[CreateEditDataType] = field(
        default=None,
        metadata={
            "name": "Edit",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    clip: Optional[CreateClipDataType] = field(
        default=None,
        metadata={
            "name": "Clip",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    compilation: Optional[CreateCompilationDataType] = field(
        default=None,
        metadata={
            "name": "Compilation",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    composite: Optional[ModifyCompositeDataType] = field(
        default=None,
        metadata={
            "name": "Composite",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    series_ancestry: Optional[SeriesAncestryType] = field(
        default=None,
        metadata={
            "name": "SeriesAncestry",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    simple_metadata: list[SimpleInfoType] = field(
        default_factory=list,
        metadata={
            "name": "SimpleMetadata",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    id: list[AssetDoitype] = field(
        default_factory=list,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    generations_above: list[int] = field(
        default_factory=list,
        metadata={
            "name": "GenerationsAbove",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    generations_below: list[int] = field(
        default_factory=list,
        metadata={
            "name": "GenerationsBelow",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    relationship_type: list[TargetRelationshipType] = field(
        default_factory=list,
        metadata={
            "name": "RelationshipType",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    relationship_class: list[
        Union[
            SupplementalContentClassType,
            AlternateContentClassType,
            PackagingClassType,
            PromotionClassType,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "name": "RelationshipClass",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    query: Optional[QueryType] = field(
        default=None,
        metadata={
            "name": "Query",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    query_results: Optional[QueryResultsType] = field(
        default=None,
        metadata={
            "name": "QueryResults",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    virtual_fields: Optional[VirtualFieldsType] = field(
        default=None,
        metadata={
            "name": "VirtualFields",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    report_query: Optional[ReportQueryType] = field(
        default=None,
        metadata={
            "name": "ReportQuery",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    report_results: Optional[ReportResultsType] = field(
        default=None,
        metadata={
            "name": "ReportResults",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
