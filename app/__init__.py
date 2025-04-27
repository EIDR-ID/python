from typing import Optional, TypedDict

class ConfigDict(TypedDict):
    url: Optional[str]
    party: Optional[str]
    user: Optional[str]
    password: Optional[str]