from pathlib import Path
from pprint import pprint

from app.manager import SessionManager
from app.scheme.org.eidr.schema import CreationType
from app.scheme.org.eidr.schema import CreateSeasonDataType
from app.services import RegistryRequest, Query
from app.services.registration.create import Create
from util import dict_to_instance, from_json, generate_templates

manager = SessionManager.from_default()
manager.template_dir = Path.cwd() / 'gen_records'

def generate_template_files():
    generate_templates(Path(manager.template_dir)[CreationType.CREATE_BASIC])
    print("Template file(s) have been generated")

def query_series():
    exp = Query.base_obj_expression(
        resource_name="The Kroons"
    )
    q = Query(
        response_type=Query.QueryResponseType.ID,
        expression=exp,
        page_num=1,
        page_size=100
    )
    res = manager.query(RegistryRequest(
        operations=[q]
    ))
    print(res)

def create_season():
    data = from_json(Path(manager.template_dir / "create_season.json"))
    rec =  dict_to_instance(data, CreateSeasonDataType)
    rec.base_object_data.administrators.registrant.value = manager.driver.config.party
    season = Create(record=rec)
    req = RegistryRequest([season])
    resp = manager.register(req, True)
    print("Season Record Response:")
    pprint(resp)

if __name__ == "__main__":
    # query_series()
    # create_season()
    generate_template_files()