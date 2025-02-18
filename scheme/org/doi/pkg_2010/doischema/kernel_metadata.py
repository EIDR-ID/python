from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

from scheme.org.doi.pkg_2010.doischema.referent_creation import (
    ReferentCreation,
)
from scheme.org.doi.pkg_2010.doischema.referent_party import ReferentParty
from scheme.org.doi.pkg_2010.doischema_avs.primary_referent_type import (
    PrimaryReferentType,
)

__NAMESPACE__ = "http://www.doi.org/2010/DOISchema"


@dataclass
class KernelMetadata:
    """
    The XML schema for DOI Kernel metadata.

    :ivar referent_doi_name: The specific DOI name allocated to the
        referent.
    :ivar primary_referent_type: The primaryReferentType of the referent
        (Creation or Party).
    :ivar registration_agency_doi_name: The DOI name of the Registration
        Agency responsible for issuing this Declaration.
    :ivar issue_date: The date on which this Declaration was issued.
    :ivar issue_number: The sequence number of this Declaration in the
        series of Kernel Metadata Declarations issued for this DOI name.
        Original issue=1. If a Kernel Metadata Declaration for a
        specific DOI name is re-issued, this number should be
        incremented by one.
    :ivar referent_creation: The creation identified by the DOI name
        (where the primary referentType is 'Creation').
    :ivar referent_party: The party identified by the DOI name (where
        the primary referentType is 'Party').
    """

    class Meta:
        name = "kernelMetadata"
        namespace = "http://www.doi.org/2010/DOISchema"

    referent_doi_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "referentDoiName",
            "type": "Element",
            "required": True,
            "pattern": r"10\.[^\./@]+(\.[^\./@]+)*/.+",
        },
    )
    primary_referent_type: Optional[PrimaryReferentType] = field(
        default=None,
        metadata={
            "name": "primaryReferentType",
            "type": "Element",
            "required": True,
        },
    )
    registration_agency_doi_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "registrationAgencyDoiName",
            "type": "Element",
            "required": True,
            "pattern": r"10\.[^\./@]+(\.[^\./@]+)*/.+",
        },
    )
    issue_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "issueDate",
            "type": "Element",
            "required": True,
        },
    )
    issue_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "issueNumber",
            "type": "Element",
            "required": True,
        },
    )
    referent_creation: Optional[ReferentCreation] = field(
        default=None,
        metadata={
            "name": "referentCreation",
            "type": "Element",
        },
    )
    referent_party: Optional[ReferentParty] = field(
        default=None,
        metadata={
            "name": "referentParty",
            "type": "Element",
        },
    )
