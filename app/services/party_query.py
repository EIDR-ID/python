from abc import ABC
from typing import Optional

from app.services.interface import ServiceBase

from app.scheme.org.eidr.schema import operation_type, asset_doitype, expression_service_query_type, find_services
from app.services.no_op import NoOperationRequest


class PartyQuery(NoOperationRequest):
    """
    Represents a service for querying party information.

    This service allows querying party details using various parameters such as
    ID, display name, organization ID, and more. It extends the `NoOperationRequest`
    base class.
    """
    name = "party/query"

    def __init__(self, expression: Optional[str] = None, page_number: Optional[int] = 1, page_size: Optional[int] = 1, continuation_token: Optional[str] = None):
        """
        Initializes the PartyQuery service with optional query parameters.

        Args:
            expression (Optional[str]): The query expression.
            page_number (Optional[int]): The page number for pagination. Defaults to 1.
            page_size (Optional[int]): The number of results per page. Defaults to 1.
            continuation_token (Optional[str]): Token for continuing a previous query.
        """
        super().__init__(
            expression=expression,
            page_number=page_number,
            page_size=page_size,
            continuation_token=continuation_token
        )

    def validate(self) -> bool:
        """
        Validates the query parameters.

        Returns:
            bool: Always returns True as validation is not implemented.
        """
        return True

    def objectify(self):
        """
        Converts the query parameters into the internal representation.

        This method creates a `FindServices` object using the provided arguments.

        Raises:
            ValueError: If invalid arguments are provided.
        """
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
            alternate_party_name: str | None = None,
            contact_name: str | None = None,
            primary_email: str | None = None,
            alternate_email: str | None = None,
            contact_address: str | None = None,
            contact_phone: str | None = None,
            active: bool | None = None,
            party_account_name: str | None = None,
            allowed_roles: str | None = None,
    ) -> str:
        """
        Builds a query expression for party parameters.

        Args:
            id (str | None): The party ID.
            display_name (str | None): The display name of the party.
            sort_name (str | None): The sort name of the party.
            organization_id (str | None): The organization ID of the party.
            id_type (str | None): The type of the party ID.
            alternate_party_name (str | None): Alternate name of the party.
            contact_name (str | None): Contact name of the party.
            primary_email (str | None): Primary email of the party.
            alternate_email (str | None): Alternate email of the party.
            contact_address (str | None): Contact address of the party.
            contact_phone (str | None): Contact phone number of the party.
            active (bool | None): Whether the party is active.
            party_account_name (str | None): Account name of the party.
            allowed_roles (str | None): Allowed roles for the party.

        Returns:
            str: A query expression string combining all provided parameters.
        """
        party_param_mapping = [
            (id, "ID"),
            (display_name, "PartyName/DisplayName"),
            (sort_name, "PartyName/SortName"),
            (organization_id, "PartyName/OrganizationID"),
            (id_type, "PartyName/IdType"),
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

        party_clauses = [
            f'(/Party/{key} "{value}")'
            for value, key in party_param_mapping
            if value is not None
        ]

        return " AND ".join(party_clauses) if party_clauses else ""