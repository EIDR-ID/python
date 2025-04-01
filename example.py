from typing import Tuple, Any

from app.manager import (
    SessionManager,
    API_Driver,
    RegistryRequest,
    SimpleMetadata,
    # GraphTraversal
)
from app.scheme.org.eidr.schema.referent_type import ReferentType
from app.scheme.org.eidr.schema import StatusTypeType
from app.services import Query

driver: API_Driver = API_Driver.from_default()
session: SessionManager = SessionManager(driver=driver)

exp = Query.base_obj_expression(
    resource_name="The Flash",
)
q = Query(
    expression=exp,
    page_num=1,
    page_size=25
)
res = RegistryRequest(
    operations=[q]
)


match, _ = session.query(res)
for metadata in match:
    name = metadata.resource_name
    print("Name:{} doi:{}\n".format(name,metadata.doi))
    ancestor_request, err = metadata.find_ancestors(
        referent_type_filter=[ReferentType.MOVIE]
    )
    if err is not None:
        print("Error finding ancestor\n", err)
    else:
        ancestors: list[SimpleMetadata] = ancestor_request.get_simple_metaData()
        for ancestor in ancestors:
            print("{}'s Ancestor: {} Doi: {}\n".format(name,ancestor.resource_name, ancestor.doi))
    descendants_request, err = metadata.find_descendants()
    if err is not None:
        print("Error finding Dependent", err)
    else:
        descendants: list[SimpleMetadata] = descendants_request.get_simple_metaData()
        for descendant in descendants:
            print("{}'s descendant: {} Doi: {}\n".format(name,descendant.resource_name, descendant.doi))

    series_ancestry, err = metadata.get_children()
    if err is not None:
        print("Error finding Dependent", err)
    else:
        series: list[SimpleMetadata] = series_ancestry.get_simple_metaData()
        for episode in series:
            print("{}'s Episode: {} || Doi: {}\n".format(name,episode.resource_name, episode.doi))
