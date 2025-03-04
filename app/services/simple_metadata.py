import app.services.res as ResponseReader
from app.scheme.org.doi.pkg_2010.doischema_avs import CreationStructuralType
from app.scheme.org.eidr.schema import ReferentType, RelationshipType
from app.scheme.org.eidr.schema.simple_info import SimpleInfo

from app.services.graph_traversal import GraphTraversal
from app.driver import API_Driver


class SimpleMetadata(GraphTraversal):
    def __init__(self, info: SimpleInfo, driver: API_Driver):
        super().__init__(driver)
        obj = info
        self.status = obj.status.value
        self.structural_type = obj.structural_type.value
        self.id = obj.id.value
        self.doi = self.id
        self.referent_type = obj.referent_type.value
        self.release_date = obj.release_date.year
        self.original_language = [l.value for l in obj.original_language]
        self.relationship = [{"type": r.type_value.value, "value": r.value} for r in obj.relationship]
        self.resource_name = obj.resource_name.value
        self.resource_name_lang = obj.resource_name.lang
        self.version_language = [lang.value for lang in obj.version_language]

    def as_dict(self):
        return {
            "status": self.status,
            "structural_type": self.structural_type,
            "id": self.id,
            "referent_type": self.referent_type,
            "release_date": self.release_date,
            "original_language": self.original_language,
            "relationship": self.relationship,
            "resource_name": self.resource_name,
            "resource_name_lang": self.resource_name_lang,
            "version_language": self.version_language,
        }

    def pull(self, driver: API_Driver) -> ResponseReader:
        from app.services.graph_traversal import GraphTraversal
        newGraph = GraphTraversal(driver)
        return newGraph.find_ancestors(self.id)

    # def find_ancestors(
    #         self,
    #         graph: GraphTraversal,
    #         referent_type_filter: list[ReferentType] = None,
    #         relationship_type_filter: list[RelationshipType] = None,
    #         structural_type_filter: list[CreationStructuralType] = None,
    #
    # ) -> ResponseReader:
    #     from app.services.graph_traversal import GraphTraversal
    #     return graph.find_ancestors(
    #         self.id,
    #         referent_type_filter=referent_type_filter,
    #         relationship_type_filter=relationship_type_filter
    #     )
