from pathlib import Path
from pprint import pprint

from app.manager import SessionManager
from app.scheme.org.eidr.schema import CreationType
from app.services import RegistryRequest
from app.services.registration.create import Create
from scheme.org.eidr.schema import CreateBasicDataType
from util import generate_templates
"""
This script demonstrates the create operation of the registration service, provided by the EIDR API.
"""

manager = SessionManager.from_default()
template_path = Path.cwd() / "gen_records"


def create_basic():
    """
    Demonstrates how to create a basic record using the EIDR API.
    :return: None
    """
    basic = Create.from_json(template_path, CreateBasicDataType)
    req = RegistryRequest([basic])
    resp = manager.register(req, True)
    print("Season Record Response:")
    pprint(resp)

if __name__ == "__main__":
    # create_basic()
    generate_templates(template_path, [CreationType.CREATE_BASIC], )
    ...
