from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import (
    XmlDate,
    XmlDateTime,
    XmlDuration,
    XmlPeriod,
    XmlTime,
)

from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.content_identifier_type import (
    ContentIdentifierType,
)
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.money_type import MoneyType
from  app.scheme.com.movielabs.schema.md.v2.pkg_8.md.region_type import RegionType

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class TermsType:
    class Meta:
        name = "Terms-type"

    money: Optional[MoneyType] = field(
        default=None,
        metadata={
            "name": "Money",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    event: Optional[Union[XmlDateTime, XmlDate]] = field(
        default=None,
        metadata={
            "name": "Event",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    boolean: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Boolean",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    alt_identifier: Optional[ContentIdentifierType] = field(
        default=None,
        metadata={
            "name": "AltIdentifier",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    year_date_time: Optional[Union[XmlPeriod, XmlDate, XmlDateTime]] = field(
        default=None,
        metadata={
            "name": "YearDateTime",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "Time",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    region: Optional[RegionType] = field(
        default=None,
        metadata={
            "name": "Region",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    other_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    term_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "termName",
            "type": "Attribute",
            "required": True,
        },
    )
