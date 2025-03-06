import unittest

from app.driver import API_Driver, to_pretty_xml
from app.services.res import ResponseReader
from app.scheme.org.eidr.schema import CreateSeriesDataType
from app.services.registration import Registration
from app.services.meta_data_builders import BaseObjectDataBuilder, SeriesInfoBuilder

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

    def test_register_series(self):
        driver = API_Driver.from_default()

        base_object_data = (
            BaseObjectDataBuilder
            .set_structural_type("Abstraction")
            .set_mode_type("AudioVisual")
            .set_referent_type("Series")
            .set_resource_name(value="UA's 3rd Reich Von Stronberg", lang="en")
            .set_release_date("2025-03-05")
            .add_original_language(value="en", mode="Audio", language_track_type="primary")
            .set_country_of_origin(["US"])
            .set_status("valid")
            .set_approximate_length(approx_length="PT10H11M22S")
            .set_administrators(registrant=driver.config.party)
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
                series_info= extra_object_data,
            )
        )

        request = Registration(record=series_test)
        print(f"example request: \n {request.xml}")
        resp = driver.post(request)
        print(to_pretty_xml(resp.content))

        # test for successful interaction with EIDR API
        self.assertEqual(200, resp.status_code)
