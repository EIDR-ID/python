from abc import ABC
from typing import Optional

from app.services.interface import ServiceBase

from app.scheme.org.eidr.schema import operation_type, asset_doitype, expression_service_query_type, find_services
from app.services.no_op import NoOperationRequest




class ServiceQuery(NoOperationRequest):
    """
        Service for querying content delivery services present in the EIDR API.
    """
    name = "service/query"

    def __init__(self, expression: Optional[str] = None, page_number: Optional[int] = 1, page_size: Optional[int] = 1, continuation_token: Optional[str] = None):
        """
            Initialize a ServiceQuery instance for retrieving service records.

            Parameters:
                expression (Optional[str]): An XPath or search expression to filter services; defaults to None.
                page_number (Optional[int]): The page index for paginated results; must be ≥ 1. Defaults to 1.
                page_size (Optional[int]): The number of items per page; must be ≥ 1. Defaults to 1.
                continuation_token (Optional[str]): A token to continue a previous paginated query; defaults to None.
        """

        super().__init__(
            expression=expression,
            page_number=page_number,
            page_size=page_size,
            continuation_token=continuation_token
        )

    def validate(self) -> bool:
        return True

    def objectify(self):
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
    def service_expression(
            cls,
            id: str | None = None,
            display_name: str | None = None,
            alternate_service_name: str | None = None,
            description: str | None = None,
            other_affiliation: str | None = None,
            active: str | None = None,
            primary_time_zone: str | None = None,
            region: str | None = None,
            primary_audio_language: str | None = None,
            delivery_model: str | None = None,
    ) -> str:
        """
                Build an XPath query expression for Service resources.

                Parameters:
                    id (str | None): Filter by the Service ID.
                    display_name (str | None): Filter by the service’s DisplayName.
                    alternate_service_name (str | None): Filter by AlternateServiceName.
                    description (str | None): Filter by service Description.
                    other_affiliation (str | None): Filter by OtherAffiliation.
                    active (str | None): Filter by Active status.
                    primary_time_zone (str | None): Filter by PrimaryTimeZone.
                    region (str | None): Filter by Region.
                    primary_audio_language (str | None): Filter by PrimaryAudioLanguage.
                    delivery_model (str | None): Filter by DeliveryModel.

                Returns:
                    str: A combined XPath clause string using " AND " between each filter,
                         or an empty string if no parameters are provided.
        """
        # Map Service parameters to their keys.
        service_param_mapping = [
            (id, "ID"),
            (display_name, "ServiceName/DisplayName"),
            (alternate_service_name, "AlternateServiceName"),
            (description, "Description"),
            (other_affiliation, "OtherAffiliation"),
            (active, "Active"),
            (primary_time_zone, "PrimaryTimeZone"),
            (region, "Region"),
            (primary_audio_language, "PrimaryAudioLanguage"),
            (delivery_model, "DeliveryModel"),
        ]

        # Build query clauses for each provided parameter.
        clauses = [
            f'(/Service/{key} "{value}")'
            for value, key in service_param_mapping if value is not None
        ]

        return " AND ".join(clauses) if clauses else ""
    @classmethod
    def kernel_metadata_expression(
            cls,
            referent_doi_name: str | None = None,
            primary_referent_type: str | None = None,
            registration_agency_doi_name: str | None = None,
            issue_date: str | None = None,
            issue_number: str | None = None,
            party_principal_name: str | None = None,
            party_abbreviated_name: str | None = None,
            party_structural_type: str | None = None,
            associated_role: str | None = None,
            associated_territory: str | None = None,
    ) -> str:
        """
        Build an XPath query expression for KernelMetadata resources.
        :param referent_doi_name: Referent name according to DOI
        :param primary_referent_type: Referent type
        :param registration_agency_doi_name: Name of the registration agency according to DOI
        :param issue_date: Date of issue
        :param issue_number: Issue number
        :param party_principal_name: Principal name of the party tied to this service
        :param party_abbreviated_name: Abbreviated name of the party tied to this service
        :param party_structural_type: Structural type of the relevant party
        :param associated_role: Role of the service
        :param associated_territory: Territory associated with the service
        :return: A combined XPath clause string using " AND " between each filter,
        """
        # Map kernel metadata parameters to their keys.
        kernel_param_mapping = [
            (referent_doi_name, "referentDoiName"),
            (primary_referent_type, "primaryReferentType"),
            (registration_agency_doi_name, "registrationAgencyDoiName"),
            (issue_date, "issueDate"),
            (issue_number, "issueNumber"),
        ]

        # Build query clauses for top-level kernel metadata.
        kernel_clauses = [
            f'(/KernelMetadata/{key} "{value}")'
            for value, key in kernel_param_mapping
            if value is not None
        ]

        # Map referentParty parameters to their keys.
        party_param_mapping = [
            (party_principal_name, "name[PrincipalName]"),
            (party_abbreviated_name, "name[AbbreviatedName]"),
            (party_structural_type, "structuralType"),
            (associated_role, "associatedRole"),
            (associated_territory, "associatedTerritory"),
        ]

        # Build query clauses for referentParty.
        party_clauses = [
            f'(/KernelMetadata/referentParty/{key} "{value}")'
            for value, key in party_param_mapping
            if value is not None
        ]

        # Combine both clause sets.
        clauses = kernel_clauses + party_clauses
        return " AND ".join(clauses) if clauses else ""
