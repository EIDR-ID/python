import re

from app.scheme.org.eidr.schema import RegistrantType, OperationType
from app.scheme.org.eidr.schema.request_status_type import RequestStatusType
from app.services.interface import ServiceBase

status_options = ["success", "duplicate", "pending", "authorization error", "validation error", "other error", "rejected"]
class StatusRequest(ServiceBase):
    """
    Represents a request to query the status of an operation.

    Attributes:
        name (str): The name of the service.

    """

    name = "status"

    def __init__(self,
                 token: str | None = None,
                 user_id: str | None = None,
                 registrant: str | None = None,
                 status: str | None = None,
                 page_size: int = 1,
                 page_number: int = 1,
                 after: str | None = None,
                 to: str | None = None,
                 from_value: str | None = None,
                 continuation_token: str | None = None):
        """
        Initializes a StatusRequest instance.

        Args:
            token (str | None): The authentication token.
            user_id (str | None): The ID of the user making the request.
            registrant (str | None): The registrant identifier.
            status (str | None): The status to query. Must be one of the allowed status options.
            page_size (int): The number of results per page. Defaults to 1.
            page_number (int): The page number to retrieve. Defaults to 1.
            after (str | None): The starting point for the query.
            to (str | None): The end point for the query.
            from_value (str | None): The starting value for the query.
            continuation_token (str | None): A token to continue a previous query.

        Raises:
            ValueError: If the status is invalid or the registrant does not match the required format.
        """
        if status and status not in status_options:
            raise ValueError("Invalid status, must be one of {}".format(status_options))
        regex = r"10\.5237/[0-9a-fA-F]{4}-[0-9a-fA-F]{4}|10\.5237/superparty"
        if registrant and re.match(regex, registrant) is None:
            raise ValueError("Invalid registrant type")
        super().__init__(token=token, user_id=user_id, registrant_type=registrant, status=status, page_size=page_size,
                         page_number=page_number, after=after, to=to, from_value=from_value, continuation_token=continuation_token)

    def objectify(self):
        """
        Converts the request parameters into an object representation.

        This method creates an `OperationType` object with the provided arguments.
        """
        reg = self.args.get("registrant_type")
        self.obj = OperationType(
            status_request=RequestStatusType(
                page_size=self.args.get("page_size"),
                page_number=self.args.get("page_number"),
                continuation_token=self.args.get("continuation_token"),
                token=self.args.get("token"),
                user_id=self.args.get("user_id"),
                status=self.args.get("status"),
                registrant=RegistrantType(reg) if reg else None,
                after=self.args.get("after"),
                to=self.args.get("to"),
                from_value=self.args.get("from_value"),
            )
        )

    def validate(self) -> bool:
        """
        Validates the request.

        Returns:
            bool: Always returns True. not implemented.
        """
        return True