import unittest

from pprint import pprint

from app.manager import SessionManager
import app.driver as driver
from services import RegistryRequest
from services.registration.add_relationship import AddRelationship
from services.registration.alias import Alias

from services.registration.create import Create
from services.registration.modify import Modify
from services.registration.promote import Promote
from services.registration.replace_relationship import ReplaceRelationship

from util import from_json, dict_to_dataclass


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
        data = from_json("create_basic.json")
        r =  dict_to_dataclass(cls="create_basic", data=data)
        r.base_object_data.administrators.registrant.value = self.manager.driver.config.party
        basic = Create(record=r)
        req = RegistryRequest([basic])
        resp = self.manager.register(req, True)
        print("Basic Record Response:")
        pprint(resp)

    def test_register_series(self):
        data = from_json("create_series.json")
        r =  dict_to_dataclass(cls="create_series", data=data)
        r.base_object_data.administrators.registrant.value = self.manager.driver.config.party
        series = Create(record=r)
        req = RegistryRequest([series])
        resp = self.manager.register(req, True)
        print("Series Record Response:")
        pprint(resp)

    def test_register_season(self):
        data = from_json("create_season.json")
        r =  dict_to_dataclass(cls="create_season", data=data)
        r.base_object_data.administrators.registrant.value = self.manager.driver.config.party
        season = Create(record=r)
        req = RegistryRequest([season])
        resp = self.manager.register(req, True)
        print("Season Record Response:")
        pprint(resp)

    def test_register_episode(self):
        data = from_json("create_episode.json")
        r =  dict_to_dataclass(cls="create_episode", data=data)
        r.base_object_data.administrators.registrant.value = self.manager.driver.config.party
        episode = Create(record=r)
        req = RegistryRequest([episode])
        resp = self.manager.register(req, True)
        print("Episode Record Response:")
        pprint(resp)

    # def test_register_clip(self):
    #     data = from_json("create_clip.json")
    #     r =  dict_to_dataclass(cls="create_clip", data=data)
    #     r.base_object_data.administrators.registrant.value = self.manager.driver.config.party
    #     clip = Create(record=r)
    #     req = RegistryRequest([clip])
    #     resp = self.manager.register(req, True)
    #     print("Clip Record Response:")
    #     pprint(resp)

    def test_register_compilation(self):
        data = from_json("create_compilation.json")
        r =  dict_to_dataclass(cls="create_compilation", data=data)
        r.base_object_data.administrators.registrant.value = self.manager.driver.config.party
        compilation = Create(record=r)
        req = RegistryRequest([compilation])
        resp = self.manager.register(req, True)
        print("Compilation Record Response:")
        pprint(resp)

    # TODO: Debug registry syntax error: "Cannot resolve 'CreateEdit' to a type definition for element 'Edit'
    # def test_register_edit(self):
    #     data = from_json("create_edit.json")
    #     r =  dict_to_dataclass(cls="create_edit", data=data)
    #     r.base_object_data.administrators.registrant.value = self.manager.driver.config.party
    #     edit = Create(record=r)
    #     req = RegistryRequest([edit])
    #     resp = self.manager.register_create(req, True)
    #     print("Edit Record Response:")
    #     pprint(resp)

    # TODO: configure valid manifestation record
    # def test_register_manifestation(self):
    #     data = from_json("create_manifestation.json")
    #     r =  dict_to_dataclass(cls="create_manifestation", data=data)
    #     r.base_object_data.administrators.registrant.value = self.manager.driver.config.party
    #     season_record = Create(record=r)
    #     req = RegistryRequest([season_record])
    #     resp = self.manager.register_create(req, True)
    #     print("Series Record Response:")
    #     pprint(resp)

    # TODO: Debug registry syntax error: "Cannot resolve 'Composite' to a type definition for element 'Composite'
    # def test_register_composite(self):
    #     data = from_json("create_composite.json")
    #     r =  dict_to_dataclass(cls="create_composite", data=data)
    #     r.base_object_data.administrators.registrant.value = self.manager.driver.config.party
    #     composite = Create(record=r)
    #     req = RegistryRequest([composite])
    #     resp = self.manager.register(req, True)
    #     print("Composite Record Response:")
    #     pprint(resp)

    # TODO: Debug serialization errors for all of the following tests
    # def test_add_relationship(self):
    #     data = from_json("add_relationship.json")
    #     r =  dict_to_dataclass(cls="add_relationship", data=data)
    #     add_relation = AddRelationship(relationship=r)
    #     req = RegistryRequest([add_relation])
    #     resp = self.manager.register(req, True)
    #     print("Add Relationship Operation Response:")
    #     pprint(resp)
    #
    # def test_remove_relationship(self):
    #     data = from_json("remove_relationship.json")
    #     r =  dict_to_dataclass(cls="remove_relationship", data=data)
    #     r.base_object_data.administrators.registrant.value = self.manager.driver.config.party
    #     season_record = Create(record=r)
    #     req = RegistryRequest([season_record])
    #     resp = self.manager.register(req, True)
    #     print("Remove Relationship Operation Response:")
    #     pprint(resp)
    #
    # def test_replace_relationship(self):
    #     data = from_json("replace_relationship.json")
    #     r =  dict_to_dataclass(cls="replace_relationship", data=data)
    #     season_record = ReplaceRelationship(record=r)
    #     req = RegistryRequest([season_record])
    #     resp = self.manager.register(req, True)
    #     print("Replace Relationship Operation Response:")
    #     pprint(resp)
    #
    # def test_modify(self):
    #     data = from_json("modify.json")
    #     r =  dict_to_dataclass(cls="modify", data=data)
    #     r.basic.base_object_data.administrators.registrant.value = self.manager.driver.config.party
    #     modify = Modify(record=r)
    #     req = RegistryRequest([modify])
    #     resp = self.manager.register(req, True)
    #     print("Modify Record Response:")
    #     pprint(resp)

    # def test_alias(self):
    #     alias = Alias(target_id="10.5240/0B9A-1A71-BBF3-219E-F3C7-E", id="10.5240/1B23-9602-95A2-EE0A-4090-W")
    #     req = RegistryRequest([alias])
    #     resp = self.manager.register(req, True)
    #     print("Alias Operation Response:")
    #     pprint(resp)

    # def test_promote(self):
    #     promote = Promote(id="10.5240/0B9A-1A71-BBF3-219E-F3C7-E")
    #     req = RegistryRequest([promote])
    #     resp = self.manager.register(req, True)
    #     print("Promote Operation Response:")
    #     pprint(resp)
