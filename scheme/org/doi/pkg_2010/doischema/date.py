from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

from scheme.org.doi.pkg_2010.doischema_avs.time_proximity import TimeProximity

__NAMESPACE__ = "http://www.doi.org/2010/DOISchema"


@dataclass
class Date:
    """
    A complex element describing a date.

    :ivar value: The value of the date (for example, '1967').
    :ivar proximity: The proximity of the declared date to the actual
        date (for example, 'circa', 'not before'). A null value
        indicates that the date is accurate.
    """

    class Meta:
        name = "date"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.doi.org/2010/DOISchema",
            "required": True,
        },
    )
    proximity: Optional[TimeProximity] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
