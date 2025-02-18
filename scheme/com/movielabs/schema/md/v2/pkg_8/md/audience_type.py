from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod

from scheme.com.movielabs.schema.md.v2.pkg_8.md.content_identifier_type import (
    ContentIdentifierType,
)
from scheme.com.movielabs.schema.md.v2.pkg_8.md.terms_type import TermsType

__NAMESPACE__ = "http://www.movielabs.com/schema/md/v2.8/md"


@dataclass
class AudienceType:
    class Meta:
        name = "Audience-type"

    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    who: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Who",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    when: list["AudienceType.When"] = field(
        default_factory=list,
        metadata={
            "name": "When",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    what: list["AudienceType.What"] = field(
        default_factory=list,
        metadata={
            "name": "What",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    identification: list[ContentIdentifierType] = field(
        default_factory=list,
        metadata={
            "name": "Identification",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )
    terms: list[TermsType] = field(
        default_factory=list,
        metadata={
            "name": "Terms",
            "type": "Element",
            "namespace": "http://www.movielabs.com/schema/md/v2.8/md",
        },
    )

    @dataclass
    class When:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        start_date: Optional[Union[XmlPeriod, XmlDate, XmlDateTime]] = field(
            default=None,
            metadata={
                "name": "startDate",
                "type": "Attribute",
            },
        )
        end_date: Optional[Union[XmlPeriod, XmlDate, XmlDateTime]] = field(
            default=None,
            metadata={
                "name": "endDate",
                "type": "Attribute",
            },
        )

    @dataclass
    class What:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        bonus: Optional[bool] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        condition: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
