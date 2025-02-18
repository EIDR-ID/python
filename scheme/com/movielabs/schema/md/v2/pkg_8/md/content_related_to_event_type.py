from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlDuration, XmlPeriod

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class ContentRelatedToEventType:
    """
    :ivar type_value: Battle, Crime, etc.
    :ivar sub_type:
    :ivar date:
    :ivar duration:
    :ivar description:
    :ivar primary:
    :ivar fictional:
    """

    class Meta:
        name = "ContentRelatedToEvent-type"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    sub_type: list[str] = field(
        default_factory=list,
        metadata={
            "name": "SubType",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    date: Optional["ContentRelatedToEventType.Date"] = field(
        default=None,
        metadata={
            "name": "Date",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    duration: Optional["ContentRelatedToEventType.Duration"] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    description: list["ContentRelatedToEventType.Description"] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    primary: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    fictional: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class Date:
        value: Optional[Union[XmlPeriod, XmlDate, XmlDateTime]] = field(
            default=None
        )
        approximate: Optional[bool] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Duration:
        value: Optional[XmlDuration] = field(
            default=None,
            metadata={
                "required": True,
            },
        )
        approximate: Optional[bool] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Description:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        language: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
