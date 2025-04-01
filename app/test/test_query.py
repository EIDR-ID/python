from app.manager import SessionManager
from app.scheme.org.eidr.schema import TimeZoneType
from app.services import Query, RegistryRequest
from app.services.party_query import PartyQuery
from app.services.service_query import ServiceQuery
import unittest

class TestQuery(unittest.TestCase):
    def test_party_query(self):
        ses = SessionManager.from_default()
        query = PartyQuery(
            expression=PartyQuery.party_expression(
                display_name="Columbia Pictures",
            ), page_size=1, page_number=1
        )
        res = ses.party_query(query)
        self.assertEqual(res[0].id, '10.5237/D9C6-0CD1')

    def test_service_query(self):
        ses = SessionManager.from_default()
        exp = ServiceQuery.service_expression(
            primary_time_zone="MST"
        )
        sq = ServiceQuery(
            page_number=1,
            page_size=5,
            expression=exp
        )
        query_res = ses.service_query(sq)
        self.assertEqual(query_res[0].primary_time_zone, TimeZoneType.MST)

    def test_query(self):
        ses = SessionManager.from_default()
        exp = Query.base_obj_expression(
            release_date="2017",
        )
        q = RegistryRequest(
            operations=[Query(
                expression=exp,
                page_num=1,
                page_size=15
            )]
        )
        res, _ = ses.query(q) # We don't care about the continuation token
        self.assertGreater(len(res), 0)




