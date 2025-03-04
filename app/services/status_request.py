import re

from app.scheme.org.eidr.schema import RegistrantType, OperationType
from app.scheme.org.eidr.schema.request_status_type import RequestStatusType
from app.services.interface import ServiceBase

status_options = ["success", "duplicate", "pending", "authorization error", "validation error", "other error", "rejected"]
class StatusRequest(ServiceBase):
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
                 from_value: str | None = None):
        if status and status not in status_options:
            raise ValueError("Invalid status, must be one of {}".format(status_options))
        regex = r"10\.5237/[0-9a-fA-F]{4}-[0-9a-fA-F]{4}|10\.5237/superparty"
        if registrant and re.match(regex, registrant) is None:
            raise ValueError("Invalid registrant type")
        super().__init__(token=token, user_id=user_id, registrant_type=registrant, status=status, page_size=page_size,
                         page_number=page_number, after=after, to=to, from_value=from_value)

    def objectify(self):
        self.obj = OperationType(
            status_request = RequestStatusType(
            token=self.args.get("token"),
            user_id=self.args.get("user_id"),
            status=self.args.get("status"),
            registrant=RegistrantType(self.args.get("registrant_type")),
            page_size=self.args.get("page_size"),
            page_number=self.args.get("page_number"),
            after=self.args.get("after"),
            to=self.args.get("to"),
            from_value=self.args.get("from_value"),
        ))

    def validate(self) -> bool:
        return True
