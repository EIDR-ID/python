from enum import Enum

__NAMESPACE__ = "http://www.eidr.org/schema"


class StatusTypeType(Enum):
    """The status types that correspond to the first class of statuses: success or failure state of the request at the API level"""

    SUCCESS = "success"
    SYSTEM_ERROR = "system error"
    REGISTRY_IN_READ_ONLY_ERROR = "registry in read-only error"
    INVALID_REQUEST = "invalid request"
    AUTHENTICATION_ERROR = "authentication error"
    AUTHORIZATION_ERROR = "authorization error"
    BAD_TOKEN_ERROR = "bad token error"
    BAD_QUERY_ERROR = "bad query error"
    BAD_ID_ERROR = "bad id error"
    SYNTAX_ERROR = "syntax error"
    RESULT_TOO_LONG = "result too long"
    DUPLICATE_PARTY = "duplicate party"
    DUPLICATE_USER = "duplicate user"
    BAD_PARTY = "bad party"
    BAD_USER = "bad user"
    ALL_VALID = "all valid"
    WRONG_GROUP = "wrong group"
    INVALID = "invalid"
    NO_PARENT = "no parent"
    NO_CHILDREN = "no children"
    HAS_DEPENDENTS = "has dependents"
    DUPLICATE_SERVICE = "duplicate service"
    BAD_SERVICE = "bad service"
    COMPATIBILITY_ERROR = "compatibility error"
