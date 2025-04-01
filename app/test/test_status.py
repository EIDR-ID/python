from app.driver import API_Driver
from app.manager import SessionManager
from app.services import RegistryRequest, StatusRequest


def test_status():
    token = "1741054324732003662"
    driver = API_Driver.from_default()
    ses = SessionManager(driver)
    s = RegistryRequest(
        operations=[StatusRequest(
            user_id="10.5238/cramos",
            page_number=1,
            page_size=10
        )]
    )
    res, _ = ses.status(s)
    assert res is not None  # Dummy assert
    for item in res:
        assert item is not None  # Dummy assert