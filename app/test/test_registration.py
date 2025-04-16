import unittest

from app.builders.creation.add_relationship_type_builder import AddRelationShipTypeBuilder
from app.builders.creation.series_info_builder import SeriesInfoBuilder
from app.scheme.org.eidr.schema import CreateSeriesDataType
from app.scheme.org.eidr.schema.creation_type import CreationType
from app.scheme.org.eidr.schema.create_basic_data_type import CreateBasicDataType
from app.scheme.org.eidr.schema.operation_status_type_type import OperationStatusTypeType
from app.scheme.org.eidr.schema.request_status_results_type import RequestStatusResultsType
from app.scheme.org.eidr.schema.asset_doitype import AssetDoitype
from app.builders.creation.base_object_builder import BaseObjectBuilder
from app.manager import SessionManager
from app.services.registration.create import Create
from app.services import RegistryRequest
from app.services import StatusRequest
import app.driver as driver


class RegistrationTest(unittest.TestCase):
    """
    Example Request:
    <?xml version="1.0"?>
        <Request xmlns="http://www.eidr.org/schema" xmlns:md="http://www.movielabs.com/md" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <Operation>
            <Create type="CreateSeries">
              <Series>
                <BaseObjectData>
                  <StructuralType>Abstraction</StructuralType>
                  <Mode>AudioVisual</Mode>
                  <ReferentType>Series</ReferentType>
                  <ResourceName lang="en">Solo Leveling</ResourceName>
                  <OriginalLanguage mode="Audio">ko</OriginalLanguage>
                  <ReleaseDate>2024-11-2003</ReleaseDate>
                  <CountryOfOrigin>JP</CountryOfOrigin>
                  <Status>valid</Status>
                  <ApproximateLength>PT10H11M22S</ApproximateLength>
                  <Administrators>
                    <Registrant>10.5237/xxxxxx</Registrant>
                  </Administrators>
                  <Credits>
                    <Director>
                      <md:DisplayName>Kishimoto</md:DisplayName>
                    </Director>
                  </Credits>
                </BaseObjectData>
                <ExtraObjectMetadata>
                  <SeriesInfo>
                    <SeriesClass>Episodic</SeriesClass>
                    <NumberRequired>false</NumberRequired>
                    <DateRequired>false</DateRequired>
                    <OriginalTitleRequired>false</OriginalTitleRequired>
                  </SeriesInfo>
                </ExtraObjectMetadata>
              </Series>
            </Create>
          </Operation>
        </Request>
    """

    @classmethod
    def setUpClass(cls):
        cls.manager = SessionManager(driver.API_Driver.from_default())

    def test_register_basic(self):
        # every new record needs a base_object_data and extra_object_metadata element
        base_object_data = (
            BaseObjectBuilder(creation_type=CreationType.CREATE_BASIC)
            .set_structural_type(structural_type="Abstraction")
            .set_mode_type("Audio")
            .set_referent_type("Movie")
            .set_resource_name(value="ua test bruh", lang="en")
            .set_release_date("2025-03-21")
            .add_original_language(value="en", mode="Audio")
            .set_country_of_origin(["US"])
            .set_status("valid")
            .set_approximate_length(approx_length="PT40M00S")
            .set_administrators(registrant=RegistrationTest.manager.driver.config.party)
            .add_director(display_name="Hitler Von Stronberg", lang="en")
            .build_creation_full_info()
        )
        basic_test = CreateBasicDataType(
            base_object_data=base_object_data,
        )
        # setup request
        create_series = Create(record=basic_test)
        req_create = RegistryRequest([create_series])
        print(f"the request: \n {req_create.xml}")
        res_create = self.manager.post(req=req_create)
        # TODO: Implement polling
        # req_status = StatusRequest(
        #     page_number=1,
        #     page_size=1,
        #     token=res_create.token
        # )
        # req_status = RegistryRequest([req_status])

    def test_create_series(self):
        asset_id_created = False
        # every record consists of a base_object_data
        base_object_data = (
            BaseObjectBuilder(creation_type=CreationType.CREATE_SERIES)
            .set_structural_type(structural_type="Abstraction")
            .set_mode_type("Audio")
            .set_referent_type("Series")
            .set_resource_name(value="capm5test", lang="en")
            .set_release_date("2025-03-21")
            .add_original_language(value="en", mode="Audio")
            .set_country_of_origin(["US"])
            .set_status("valid")
            .set_approximate_length(approx_length="PT00H00M00S")
            .set_administrators(registrant=RegistrationTest.manager.driver.config.party)
            .add_director(display_name="Madagascar Zoombay", lang="en")
            .build_creation_full_info()
        )
        extra_object_data = (
            SeriesInfoBuilder()
            .set_series_class('Episodic')
            .set_original_title_required(False)
            .set_number_required(False)
            .set_date_required(False)
            .build()
        )
        series_test = CreateSeriesDataType(
            base_object_data=base_object_data,
            extra_object_metadata=CreateSeriesDataType.ExtraObjectMetadata(
                series_info=extra_object_data,
            )
        )
        # setup request
        create_series = Create(record=series_test)
        req_register = RegistryRequest([create_series])
        print(f"the request: \n {req_register.xml}")
        res_register = self.manager.post(req=req_register)


## Google Playstore
## ALL OF DISNEY PLUS uses eidr ids
## One company used it for age rating data
## Cognisant ran case study on Warner Bros and Microsoft about
        # putting movies on Xbox (SPREADSHEETS with EIDR)
## Google using EIDR in Google search for streaming content AI knowledge graph
## Alt ids work, some ones like disney are only for devs (ROSSETTA STONE FOR CONTENT ID)
        


        # TODO: implement polling
        # req_status = StatusRequest(
        #     page_number=1,
        #     page_size=1,
        #     token=self.manager.tokens[0]
        # )
        # req_status = RegistryRequest([req_status])
        # res_status = self.manager.post(req=req_status)
        # if res_status.status[0] != 0:
        #     print(res_status.obj)
        #     raise RuntimeError(f"Got bad response {res_status.status}")
        # # # implement polling
        # # self.manager.future_status(req_status)
        # res_status_results: RequestStatusResultsType | None = res_status.get_field("request_status_results")
        # if res_status_results:
        #     if res_status_results.operation_status:
        #         while res_status_results.operation_status[0].status.type_value.value == OperationStatusTypeType.PENDING:
        #             res_status = self.manager.post(req=req_status)
        #             res_status_results = res_status.get_field("request_status_results")
        #     asset_id: AssetDoitype | None = res_status_results.operation_status[0].id
        #     if asset_id:
        #         print(f"Asset ID: {asset_id.value}")
        #         asset_id_created = True
        #     else:
        #         print("Asset ID not found in response.")
        # # bool check for whether the asset_id exists hence confirms successful creation or match
        self.assertEqual(0, res_register.status[0])

    # def test_add_relationship(self):
    #     # build the add relationshiptype  obj before the request obj
    #     relationship_builder = (
    #         AddRelationShipTypeBuilder()
    #         .set_id("")
    #     )

    # def test_remove_relationship(self):
    #     ...
    #
    # def test_replace_relationship(self):
    #     ...
    #
    # def test_modify_relationship(self):
    #     ...
    #
    # def test_alias(self):
    #     ...
    #
    # def test_promote(self):
    #     ...
