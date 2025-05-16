import unittest
from pathlib import Path
from pprint import pprint

from app.manager import SessionManager

from app.services import RegistryRequest
from app.services.registration.add_relationship import AddRelationship
from app.services.registration.alias import Alias
from app.services.registration.create import Create
from app.services.registration.modify import Modify
from app.services.registration.promote import Promote
from app.services.registration.replace_relationship import ReplaceRelationship
from app.services.registration.remove_relationship import RemoveRelationship

from app.scheme.org.eidr.schema import AddRelationshipType, CreateCompositeDataType, CreateEditDataType, \
    ModifyType, CreateBasicDataType, ReplaceRelationshipType, CreateEpisodeDataType, CreateClipDataType, \
    CreateSeriesDataType, CreateSeasonDataType, TargetRelationshipType
from services import Delete
from services.eidr_request import RegistryRequestSingle


class TestRegistration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manager = SessionManager.from_default()
        cls.record_dir = Path(__file__).parent / "records"

    def __delete_record(self, id: str):
        """
        Helper method to delete a record given an ID.
        :param id: The ID of the record to delete.
        """
        delete = Delete(id)
        req = RegistryRequestSingle(delete)
        self.manager.register_immediate(req)

    def test_register_basic_immediate(self):
        path: Path = self.record_dir / "create_basic.json"
        basic: Create = Create.from_json(path, CreateBasicDataType)
        req = RegistryRequestSingle(basic)
        resp = self.manager.register_immediate(req)
        print("Basic Record Response:")
        pprint(resp)
        self.assertEqual(0, resp.get("status")[0])
        self.__delete_record(resp.get("id"))

    def test_register_series_immediate(self):
        path = self.record_dir / "create_series.json"
        series = Create.from_json(path, CreateSeriesDataType)
        req = RegistryRequestSingle(series)
        resp = self.manager.register_immediate(req)
        print("Series Record Response:")
        pprint(resp)
        self.assertEqual(0, resp.get("status")[0])
        self.__delete_record(resp.get("id"))

    def test_register_season_immediate(self):
        path = self.record_dir / "create_season.json"
        season = Create.from_json(path, CreateSeasonDataType)
        req = RegistryRequest([season])
        resp = self.manager.register_immediate(req)
        pprint(resp)
        self.assertEqual(0, resp.get("status")[0])
        self.__delete_record(resp.get("id"))

    def test_register_episode_immediate(self):
        path = self.record_dir / "create_episode.json"
        episode = Create.from_json(path, CreateEpisodeDataType)
        req = RegistryRequestSingle(episode)
        resp = self.manager.register_immediate(req)
        pprint(resp)
        self.assertEqual(0, resp.get("status")[0])
        self.__delete_record(resp.get("id"))

    def test_register_clip_immediate(self):
        clip = Create.from_json(self.record_dir / "create_clip.json", CreateClipDataType)
        req = RegistryRequestSingle(clip)
        resp = self.manager.register_immediate(req)
        pprint(resp)
        self.assertEqual(0, resp.get("status")[0])
        self.__delete_record(resp.get("id"))

    def test_register_edit_immediate(self):
        edit = Create.from_json(self.record_dir / "create_edit.json", CreateEditDataType)
        req = RegistryRequestSingle(edit)
        resp = self.manager.register_immediate(req)
        print("Edit Record Response:")
        pprint(resp)
        self.assertEqual(0, resp.get("status")[0])
        self.__delete_record(resp.get("id"))

    # TODO: configure valid manifestation record
    # def test_register_manifestation_immediate(self):
    #     data = from_json("create_manifestation.json")
    #     r =  dict_to_instance(cls="create_manifestation", data=data)
    #     r.base_object_data.administrators.registrant.value = self.manager.driver.config.party
    #     season_record = Create(record=r)
    #     req = RegistryRequest([season_record])
    #     resp = self.manager.register_create(req, True)
    #     print("Series Record Response:")
    #     pprint(resp)

    # TODO: configure valid interactive record
    # def test_register_interactive_immediate(self):
    #     interactive =  Create.from_json()

    # def test_register_composite_immediate(self):
    #     composite = Create(record=CreateCompositeDataType())
    #     req = RegistryRequest([composite])
    #     resp = self.manager.register(req, True)
    #     print("Composite Record Response:")
    #     pprint(resp)

    # def test_add_relationship_immediate(self):
    #     add_relation = AddRelationship(relationship=AddRelationshipType())
    #     req = RegistryRequestSingle(add_relation)
    #     resp = self.manager.register_immediate(req)
    #     print("Add Relationship Operation Response:")
    #     pprint(resp)

    # def test_remove_relationship_immediate(self):
    #     remove_r = RemoveRelationship(
    #         id="10.5240/B203-F72D-7BFB-9961-2E5A-O",
    #         target_id="10.5240/0EF8-1553-2487-35CD-AF50-5",
    #         type_value=TargetRelationshipType.PROMOTIONAL_RELATIONSHIP
    #     )
    #     req = RegistryRequest([remove_r])
    #     resp = self.manager.register(req, True)
    #     print("Remove Relationship Operation Response:")
    #     pprint(resp)
    #
    # def test_replace_relationship_immediate(self):
    #     replace_r = ReplaceRelationship(relationship=ReplaceRelationshipType())
    #     req = RegistryRequest([replace_r])
    #     resp = self.manager.register(req, True)
    #     print("Replace Relationship Operation Response:")
    #     pprint(resp)

    # TODO: call modification base request and configure a valid modify response
    # def test_modify_immediate(self):
    #     # call request with modify operation
    #     modify = Modify(record=None)
    #     req = RegistryRequest([modify])
    #     resp = self.manager.register(req, True)
    #     print("Modify Record Response:")
    #     pprint(resp)

    # def test_alias_immediate(self):
    #     alias = Alias(target_id="10.5240/0B9A-1A71-BBF3-219E-F3C7-E", id="10.5240/1B23-9602-95A2-EE0A-4090-W")
    #     req = RegistryRequestSingle(alias)
    #     resp = self.manager.register_immediate(req)
    #     print("Alias Operation Response:")
    #     pprint(resp)
    #     # expects an error code of 3: authorization error because the target_id is alr aliased
    #     self.assertEqual(3, resp.get("status")[0])

    # def test_promote_immediate(self):
    #     promote = Promote(id="10.5240/7031-28FD-3DA7-7B61-D73D-O")
    #     req = RegistryRequestSingle(promote)
    #     resp = self.manager.register_immediate(req)
    #     print("Promote Operation Response:")
    #     pprint(resp)
    #     self.assertTrue(resp.id) or self.assertTrue(resp.duplicate)
