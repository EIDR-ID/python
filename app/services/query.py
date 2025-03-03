from typing import Optional

from app.services.interface import ServiceBase

from app.scheme.org.eidr.schema  import request, operation_type, query_type, asset_doitype



class Query(ServiceBase):
    name = "query"

    def __init__(self, doi: Optional[str] = None, expression: Optional[str] = None, page_num: Optional[int] = None, page_size: Optional[int] = None, continuation_token: Optional[str] = None, extended_family: Optional[bool] = None):
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
                    raise ValueError("Arg {} cannot be negative".format(arg))

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
                            ):
        if structural_type and structural_type not in ["Abstraction", "Performance", "Digital", "Physical"]:
            raise ValueError("structural_type must be one of 'Abstraction', 'Performance', 'Digital', or 'Physical'")
        if mode and mode not in ["Visual", "AudioVisual", "Audio", "Other"]:
            raise ValueError("mode must be one of 'Visual', 'AudioVisual', 'Audio', or 'Other'")

        base = ""
        name_map = {}
        if mode:
            name_map["Mode"] = mode
        if referent_type:
            name_map["ReferentType"] = referent_type
        if resource_name:
            name_map["ResourceName"] = resource_name
        if alternate_resource_name:
            name_map["AlternateResourceName"] = alternate_resource_name
        if original_language:
            name_map["OriginalLanguage"] = original_language
        if dubbed_language:
            name_map["DubbedLanguage"] = dubbed_language
        if associated_org:
            name_map["AssociatedOrg"] = associated_org
        if release_date:
            name_map["ReleaseDate"] = release_date
        if country_of_origin:
            name_map["CountryOfOrigin"] = country_of_origin
        if status:
            name_map["Status"] = status
        if approximate_length:
            name_map["ApproximateLength"] = approximate_length
        if alternate_id:
            name_map["AlternateID"] = alternate_id
        if display_name:
            name_map["DisplayName"] = display_name
        if credits:
            name_map["Credits"] = credits
        if registrant_extra:
            name_map["RegistrantExtra"] = registrant_extra
        if description:
            name_map["Description"] = description

        for name,val in name_map.items():
            if not base:
                base = "(/FullMetadata/BaseObjectData/{} \"{}\")".format(name, val)
            else:
                base += " AND (/FullMetadata/BaseObjectData/{} \"{}\")".format(name, val)

        return base
