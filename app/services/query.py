from enum import Enum
from typing import Optional

from app.services.interface import ServiceBase

from app.scheme.org.eidr.schema import request, operation_type, query_type, asset_doitype, QueryResultsType


class Query(ServiceBase):
    name = "query"
    response_type = "simple"

    class QueryResponseType(Enum):
        SIMPLE = "simple"
        ID = "ID"

    def __init__(self, doi: Optional[str] = None, expression: Optional[str] = None, page_num: Optional[int] = None, page_size: Optional[int] = None, continuation_token: Optional[str] = None, extended_family: Optional[bool] = None, response_type: QueryResponseType | str = QueryResponseType.SIMPLE):
        if isinstance(response_type, Enum):
            response_type = response_type.value
        self.response_type = response_type
        super().__init__(
            doi=doi,
            expression=expression,
            page_num=page_num,
            page_size=page_size,
            continuation_token=continuation_token,
            extended_family=extended_family
        )

    def validate(self) -> bool:
        expected = {
            "doi": Optional[str],
            "expression": Optional[str],
            "page_num": Optional[int],
            "page_size": Optional[int],
            "continuation_token": Optional[str],
            "extended_family": Optional[bool]
        }

        for arg, arg_type in expected.items():
            if arg in self.args:
                if not isinstance(self.args[arg], arg_type):
                    # Everything is optional, so we only care about bad types...
                    raise ValueError(
                        "Arg {} is of type {}, must be a {}".format(arg, type(self.args[arg]).__name__,
                                                                    arg_type.__args__[0].__name__))
                    # The nasty __args__[0] above is to get the expected type name instead of just "Optional"
                if (arg == "page_num" or arg == "page_size") and self.args[arg] < 0:
                    # ...and bad values
                    raise ValueError("Arg {} is required and must be positive".format(arg))

        return True

    def objectify(self):
        doi: Optional[str] = self.args.get("doi", None)
        expression: Optional[str] = self.args.get("expression", None)
        page_num: Optional[int] = self.args.get("page_num", None)
        page_size: Optional[int] = self.args.get("page_size", None)
        continuation_token: Optional[str] = self.args.get("continuation_token", None)
        extended_family: Optional[bool] = self.args.get("extended_family", None)
        self.obj = operation_type.OperationType(
            query=query_type.QueryType(
                id=asset_doitype.AssetDoitype(value=doi) if doi else None,
                expression=expression,
                page_number=page_num,
                page_size=page_size,
                continuation_token=continuation_token,
                extended_family=extended_family
            )
        )
# def test_query():
#     driver = API_Driver.from_default()
#     res = driver.post(Query(
#         expression="(/FullMetadata/BaseObjectData/ResourceName \"Avengers: Endgame\") AND /FullMetadata/BaseObjectData/ReferentType "
#                    "\"movie\"",
#         page_num=1,
#         page_size=1
#     ))
#     return to_pretty_xml(res.content)
#

    @classmethod
    def base_obj_expression(cls,
                            structural_type: str | None = None,
                            mode: str | None = None,
                            referent_type: str | None = None,
                            resource_name: str | None = None,
                            alternate_resource_name: str | None = None,
                            original_language: str | None = None,
                            dubbed_language: str | None = None,
                            associated_org: str | None = None,
                            release_date: str | None = None,
                            country_of_origin: str | None = None,
                            status: str | None = None,
                            approximate_length: str | None = None,
                            alternate_id: str | None = None,
                            display_name: str | None = None,
                            credits: str | None = None,
                            registrant_extra: str | None = None,
                            description: str | None = None,
                            ) -> str:
        # Parameter validation helper
        def validate_param(value: str | None, allowed: list[str], param_name: str) -> None:
            if value is not None and value not in allowed:
                allowed_str = ", ".join(f"'{v}'" for v in allowed)
                raise ValueError(f"{param_name} must be one of {allowed_str}")

        # Validate constrained parameters
        validate_param(
            structural_type,
            ["Abstraction", "Performance", "Digital", "Physical"],
            "structural_type",
        )
        validate_param(mode, ["Visual", "AudioVisual", "Audio", "Other"], "mode")

        # Map parameters to their corresponding keys
        param_key_mapping = [
            (mode, "Mode"),
            (referent_type, "ReferentType"),
            (resource_name, "ResourceName"),
            (alternate_resource_name, "AlternateResourceName"),
            (original_language, "OriginalLanguage"),
            (dubbed_language, "DubbedLanguage"),
            (associated_org, "AssociatedOrg"),
            (release_date, "ReleaseDate"),
            (country_of_origin, "CountryOfOrigin"),
            (status, "Status"),
            (approximate_length, "ApproximateLength"),
            (alternate_id, "AlternateID"),
            (display_name, "DisplayName"),
            (credits, "Credits"),
            (registrant_extra, "RegistrantExtra"),
            (description, "Description"),
        ]

        # Build query clauses
        clauses = [
            f'(/FullMetadata/BaseObjectData/{key} "{value}")'
            for value, key in param_key_mapping
            if value is not None
        ]

        return " AND ".join(clauses) if clauses else ""
