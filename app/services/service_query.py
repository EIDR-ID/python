from abc import ABC
from typing import Optional

from app.services.interface import ServiceBase

from app.scheme.org.eidr.schema import operation_type, asset_doitype, expression_service_query_type, find_services
from app.services.no_op import NoOperationRequest


class ServiceQuery(NoOperationRequest):
    name = "service/query"

    def __init__(self, expression: Optional[str] = None, page_number: Optional[int] = 1, page_size: Optional[int] = 1, continuation_token: Optional[str] = None):
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

    # def test_query():
    #     driver = API_Driver.from_default()
    #     res = driver.post(Query(
    #         expression="(/FullMetadata/BaseObjectData/ResourceName \"Avengers: Endgame\") AND /FullMetadata/BaseObjectData/ReferentType "
    #                    "\"movie\"",
    #         page_num=1,
    #         page_size=1
    #     ))
    #     return to_pretty_xml(res.content)
    #

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
