from typing import Optional

from .interface import ServiceBase

from scheme.org.eidr.schema import request, operation_type, query_type, asset_doitype


class Query(ServiceBase):
    name = "query"

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
                        "Arg {} is of type {}, must be a {}".format(arg, type(self.args[arg]).__name__, arg_type.__args__[0].__name__))
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
        self.obj = request.Request(operation=[operation_type.OperationType(
            query=query_type.QueryType(
                id=asset_doitype.AssetDoitype(value=doi) if doi else None,
                expression=expression,
                page_number=page_num,
                page_size=page_size,
                continuation_token=continuation_token,
                extended_family=extended_family
            )
        )])
