import base64
import hashlib
import os
from dataclasses import dataclass, field
from typing import Dict, Optional

from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from services import Query, ServiceBase

os.environ['default_proxy_port'] = "80"

import requests
from lxml import etree  # Suggested to use lxml for XML parsing, other option is xml.etree.ElementTree


default_proxy_port = 80


# This is a dataclass that represents the information needed for a connection to the EIDR API
@dataclass
class EIDR_Config:
    url: Optional[str] = None
    party: Optional[str] = None
    user: Optional[str] = None
    password: Optional[str] = None
    hash: Optional[str] = None
    multipart: bool = False
    boundary: str = "_EIDR MULTIPART_"
    pagesize: int = 1000
    fake_trust_manager: bool = False
    report_scores: bool = False
    retry_count: int = 3
    use_gzip: bool = False
    proxy_host: Optional[str] = None
    proxy_port: Optional[int] = None
    proxy_user: Optional[str] = None
    proxy_password: Optional[str] = None
    headers: Dict[str, str] = field(default_factory=dict)

    """
    Create an instance of EIDR_Config from an XML string.
    :param xml: XML string to parse.
    :return: EIDR_Config instance.
    """

    @classmethod
    def from_xml(cls, xml: str):
        root = etree.fromstring(xml.encode('utf-8'))
        options = {}

        for child in list(root.find('EndpointInfo')):
            options[child.tag] = child.text
        config = EIDR_Config(
            url=options.get('BaseURL'),
            party=options.get('Party'),
            user=options.get('User'),
            password=options.get('Passwd'),
        )
        return config

    def set_header(self, header: str, value: str):
        self.headers.update({header: value})

    def remove_header(self, header: str):
        self.headers.pop(header, None)

    def __post_init__(self):
        if not self.url.endswith("/"):
            self.url += "/"

        shadow = base64.b64encode(hashlib.sha256(self.password.encode('utf-8')).digest()).decode('utf8')
        auth_str = '%s:%s:%s' % (self.user, self.party, shadow)
        self.set_header('Authorization', 'Eidr {}'.format(auth_str))
        self.set_header('Accept', 'text/xml')
        if self.multipart:
            self.set_header('Content-Type', 'multipart/form-data; boundary={}'.format(self.boundary))
        else:
            self.set_header('Content-Type', 'text/xml')
        self.password = shadow

        if self.use_gzip:
            self.set_header('gzip', '')

    # TODO: This is GPT'd, either remove or fix
    def to_xml(self):
        print("You've been GPT'd!")
        root = etree.Element('EIDR_Config')
        for key, value in self.__dict__.items():
            if value:
                etree.SubElement(root, key).text = str(value)
        return etree.tostring(root, pretty_print=True)


# <!> The enum below has been swapped out with an interface/classes gimmick in the services module.
#     I'm keeping this here just for the TODOs
#
# We will need to create a class for each of the services we want to use
# Below is an enum that maps from the service name to the service endpoint
# class Service(Enum):
#     QUERY = 'query'
#     MATCH = 'match'  # TODO: do this
#     GRAPH = 'object/graph'  # TODO: do this.
#     # http params: extendedFamily = False
#     # xml: FindAncestors, FindDescendants, GetDependents, GetSeriesAncestry, GetLightweightRelationships, GetRemotestAncestor, GetLeafDescendants, GetParent, GetChildren
#     SERVICE_QUERY = 'service/query'  # TODO: do this
#     # xml: FindServices, FindServicesByName, or FindServicesFromCatalog
#     SERVICE_REGISTER = 'service/create'  # TODO: do this
#     # xml: CreateService
#     SERVICE_MODIFY = 'service/modify'  # TODO: do this
#     # xml: Service
#     PARTY_QUERY = 'party/query?type={}'  # TODO: do this
#     # url params: type = [ID | full]
#     # xml: FindParties, FindPartiesByName, FindPartiesFromCatalog
#     PASSWORD = '/user/password/{}?password={}'  # TODO: do this
#     # url params: userdoi, new password
#     STATUS = 'status'  # TODO: do this. Known as Cancellation Service also
#     # xml: Refer to schema


# TODO: GET endpoints needed:
# .../party/resolve/?type=[doi | full]
# .../user/resolve/{userdoi}?type=[doi | full]


# This is the main class that initiates a connection to EIDR and makes HTTP requests
class API_Driver:

    def __init__(self, config: EIDR_Config):
        self.config = config

    @classmethod
    def from_default(cls):
        with open("config.xml", "r") as file:
            config = EIDR_Config.from_xml(file.read())
        return API_Driver(config)

    def get_object(self, object_id):
        print(self.config.headers)

        req = self.config.url + 'object/' + object_id + '?type=Full&followAlias=true'
        resp = requests.get(req, headers=self.config.headers)
        print(resp.content)
        return resp.content

    def post(self, service: ServiceBase):
        return self.post_raw(service.xml, service.name)

    def post_raw(self, xml: str, endpoint: str):
        # multipart might be better off ignored here, assume it is always false for now
        data = xml if not self.config.multipart else (
            "{}\n{}\n{}\n{}\n{}".format(
                self.config.boundary,
                'Content-Disposition: form-data; name={}'.format(endpoint),
                'Content-Transfer-Encoding: binary',
                xml,
                self.config.boundary
            ))
        # print(self.config.headers)
        # print(data)
        resp = requests.post(
            self.config.url + endpoint + "/",
            data=data,
            headers={**self.config.headers}
        )
        if resp.status_code != 200:
            print("Error: {}".format(resp.status_code))
        else:
            ...  # print(resp.content)

        return resp


def test_get():
    with open("config.xml", "r") as file:
        config = EIDR_Config.from_xml(file.read())
    driver = API_Driver(config)
    res = driver.get_object("10.5240/0EF3-54F9-2642-0B49-6829-R")
# test_get()

def test_post_file():
    xml = ""
    with open("test_post.xml", "r") as file:
        xml = file.read()
    with open("config.xml", "r") as file:
        config = EIDR_Config.from_xml(file.read())
    driver = API_Driver(config)

    driver.post_raw(xml, "query")


# test_post_file()


def to_pretty_xml(s):
    root = etree.fromstring(s)
    return etree.tostring(root, pretty_print=True, xml_declaration=True, encoding='UTF-8').decode('utf-8')


def test_query():
    driver = API_Driver.from_default()
    res = driver.post(Query(
        expression="(/FullMetadata/BaseObjectData/ResourceName \"Avengers: Endgame\") AND /FullMetadata/BaseObjectData/ReferentType "
                   "\"movie\"",
        page_num=1,
        page_size=1
    ))
    return to_pretty_xml(res.content)


#print(test_query())
