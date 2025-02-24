from enum import Enum

__NAMESPACE__ = "http://www.doi.org/2010/DOISchemaAVS"


class ReturnType(Enum):
    """
    Allowed values for resource types (e.g. MIME types).

    :cvar APPLICATION_RDF_XML: application/rdf+xml
    :cvar APPLICATION_XML: application/xml
    :cvar TEXT_HTML: text/html
    :cvar TEXT_XML: text/xml
    """

    APPLICATION_RDF_XML = "application/rdf+xml"
    APPLICATION_XML = "application/xml"
    TEXT_HTML = "text/html"
    TEXT_XML = "text/xml"
