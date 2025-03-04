from typing import Tuple, Any

from app.manager import SessionManager, API_Driver,RegistryRequest,SimpleMetadata,ResponseReader,GraphTraversal
from app.scheme.org.eidr.schema.referent_type import ReferentType
from app.scheme.org.eidr.schema import StatusTypeType
from app.services import Query

driver: API_Driver = API_Driver.from_default()
session: SessionManager = SessionManager(driver=driver)

driver = API_Driver.from_default()
exp = Query.base_obj_expression(
    release_date="2005"
)
q=Query(
    expression=exp,
    page_num=1,
    page_size=1
)

res =RegistryRequest(
    operations=[q]
)


match,_ = session.query(res)

graph = GraphTraversal(driver)

for metadata in match:
    response: Tuple[ResponseReader, Any] = metadata.find_ancestors(
        graph=graph,
        referent_type_filter=[ReferentType.SERIES,ReferentType.SEASON]

    )
    if response[1] is not None:
        print("Error finding ancestor", response[1])
    response_reader: ResponseReader = response[0]
    print(response_reader.get_simple_metaData()[1].as_dict())

