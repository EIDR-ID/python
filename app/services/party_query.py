from abc import ABC
from typing import Optional

from app.services.interface import ServiceBase

from app.scheme.org.eidr.schema import operation_type, asset_doitype, expression_service_query_type, find_services
from app.services.no_op import NoOperationRequest


class PartyQuery(NoOperationRequest):
    name = "party/query"

    def __init__(self, expression: Optional[str] = None, page_number: Optional[int] = 1, page_size: Optional[int] = 1, continuation_token: Optional[str] = None):
        super().__init__(
            expression=expression,
            page_number=page_number,
            page_size=page_size,
            continuation_token=continuation_token
        )

    def validate(self) -> bool:

        return True

    def objectify(self):
        expression: Optional[str] = self.args.get("expression", None)
        page_number: Optional[int] = None
        try:
            page_number = self.args.get("page_number")
        except ValueError:
            page_number = self.args.get("page_num", None)
        page_size: Optional[int] = self.args.get("page_size", None)
        continuation_token: Optional[str] = self.args.get("continuation_token", None)
        self.obj = find_services.FindServices(
            expression=expression,
            page_number=page_number,
            page_size=page_size,
            continuation_token=continuation_token
        )

    @classmethod
    def party_expression(
            cls,
            id: str | None = None,
            display_name: str | None = None,
            sort_name: str | None = None,
            organization_id: str | None = None,
            id_type: str | None = None,
            alternate_party_name: str | None = None,  # Now treated as a regular string
            contact_name: str | None = None,
            primary_email: str | None = None,
            alternate_email: str | None = None,
            contact_address: str | None = None,
            contact_phone: str | None = None,

            active: bool | None = None,
            party_account_name: str | None = None,
            allowed_roles: str | None = None,  # Now treated as a regular string
    ) -> str:
        # Map Party parameters to their keys.
        party_param_mapping = [
            (id, "ID"),
            (display_name, "PartyName/DisplayName"),
            (sort_name, "PartyName/SortName"),
            (organization_id, "PartyName/OrganizationID"),
            (id_type, "PartyName/IdType"), # TODO: Is the name here right?
            (alternate_party_name, "AlternatePartyName"),
            (contact_name, "ContactInfo/Name"),
            (primary_email, "ContactInfo/PrimaryEmail"),
            (alternate_email, "ContactInfo/AlternateEmail"),
            (contact_address, "ContactInfo/Address"),
            (contact_phone, "ContactInfo/Phone/Value"),
            (active, "Active"),
            (party_account_name, "PartyAccountName"),
            (allowed_roles, "AllowedRoles"),
        ]

        # Build query clauses for Party parameters.
        party_clauses = [
            f'(/Party/{key} "{value}")'
            for value, key in party_param_mapping
            if value is not None
        ]

        return " AND ".join(party_clauses) if party_clauses else ""
