from typing import List

from lxml.html.diff import token

from app.driver import API_Driver
from app.services import RegistryRequest, ServiceBase, ResponseReader, Query

from app.test.demo import driver


class SessionManager:
    driver:API_Driver = None
    tokens:List[str] = []


    def __init__(self, driver: API_Driver):
        self.driver = driver

    def post(self, req: RegistryRequest):
        res = ResponseReader(driver.post_raw(req.xml, req.name))
        if res.token:
            self.tokens.append(res.token)
        return ResponseReader(res)






