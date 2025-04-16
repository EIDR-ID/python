from app.manager import SessionManager
from app.scheme.org.eidr.schema import TimeZoneType
from app.services import Query, RegistryRequest
from app.services.party_query import PartyQuery
from app.services.service_query import ServiceQuery
import unittest


class TestQuery(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ses = SessionManager.from_default()

    def test_party_query(self):
        query = PartyQuery(
            expression=PartyQuery.party_expression(
                display_name="Columbia Pictures",
            ), page_size=1, page_number=1
        )
        res = self.ses.party_query(query)
        self.assertEqual(res[0].id, '10.5237/D9C6-0CD1')

    def test_service_query(self):
        exp = ServiceQuery.service_expression(
            primary_time_zone="MST"
        )
        sq = ServiceQuery(
            page_number=1,
            page_size=5,
            expression=exp
        )
        query_res = self.ses.service_query(sq)
        self.assertEqual(query_res[0].primary_time_zone, TimeZoneType.MST)

    def test_query(self):
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
        res, _ = self.ses.query(q)  # We don't care about the continuation token
        self.assertGreater(len(res), 0)

if __name__ == '__main__':
    unittest.main()
