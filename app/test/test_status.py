import unittest

from app.manager import SessionManager
from app.services import RegistryRequest, StatusRequest


class TestStatus(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        from app.driver import API_Driver
        cls.ses = SessionManager(API_Driver.from_default())

    def test_status(self):
        token = "1741054324732003662"
        s = RegistryRequest(
            operations=[StatusRequest(
                user_id=self.ses.driver.config.user,
                page_number=1,
                page_size=10
            )]
        )

        res, _ = self.ses.status(s)
        self.assertNotEqual(res, None)
        for item in res:
            self.assertNotEqual(item, None)


if __name__ == "__main__":
    unittest.main()