import base64
import hashlib
import os
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, Optional

from requests import Response

from app.scheme.org.eidr.schema.asset_doitype import AssetDoitype
from app.scheme.org.eidr.schema import Request
from app.scheme.org.eidr.schema.request import RequestType
from app.config.config import CONFIG_PATH

from app.services import Query, ServiceBase, RegistryRequest, Delete
from app import ConfigDict

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

    @classmethod
    def from_dict(cls, config: ConfigDict):
           return EIDR_Config(
            url= config.get('url'),
            party= config.get('party'),
            user= config.get('user'),
            password= config.get('password'),
        )

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
class ResolveMode(Enum):
    FULL = "full"
    DOI = "doi"


class QueryMode(Enum):
    ID = "ID"
    FULL = "full"

class ACL_Type(Enum):
    MODIFY = "Modify"
    DELETE = "Delete"
    READ_ACL = "ReadACL"
    WRITE_ACL = "WriteACL"
    READ_PROV = "ReadProvenance"

class ModifyType(Enum):
    CREATE_BASIC = "CreateBasic"
    CREATE_SERIES = "CreateSeries"
    CREATE_SEASON = "CreateSeason"
    CREATE_EPISODE = "CreateEpisode"
    CREATE_CLIP = "CreateClip"
    CREATE_COMPILATION = "CreateCompilation"
    CREATE_EDIT = "CreateEdit"
    CREATE_MANIFESTATION = "CreateManifestation"
class API_Driver:

    def __init__(self, config: EIDR_Config):
        self.config = config

    @classmethod
    def from_default(cls, config_file: str = CONFIG_PATH):
        with open(config_file, "r") as file:
            config = EIDR_Config.from_xml(file.read())
        return API_Driver(config)

    @classmethod
    def from_dict(cls, config: ConfigDict):
        return API_Driver(EIDR_Config.from_dict(config))

    def get_object(self, object_id, service_doi: str | ResolveMode = ResolveMode.FULL):
        print(self.config.headers)

        req = self.config.url + 'object/' + object_id + '?type=Full&followAlias=true'
        resp = requests.get(req, headers=self.config.headers)
        # print(resp.content)
        return resp.content

    def get_video_service(self, service_id: str, service_doi: str | ResolveMode, followAlias: bool = True) -> str:
        doi_mode = service_doi
        if isinstance(doi_mode, ResolveMode):
            doi_mode = service_doi.value
        if doi_mode.lower() not in ["doi", "full"]:
            raise ValueError("Resolution mode must be either 'doi' or 'full'")
        req = self.config.url + 'service/resolve/' + service_id + '?type=' + doi_mode + '&followAlias=' + str(
            followAlias).lower()
        resp = requests.get(req, headers=self.config.headers)
        return resp.content.decode('utf-8')
        # https://registry1.eidr.org/EIDR/service/resolve/{servicedoi}?type=[doi|full]&followAlias=[true|false]

    def get_video_service_traversal(self, service_doi: AssetDoitype, service_endpoint: str,
                                    all_children: bool) -> Response:
        service_url = "service/{}/{}".format(service_endpoint, service_doi.value)
        if all_children:
            service_url += "?allChildren=true"
        req = self.config.url + service_url
        resp = requests.get(req, headers=self.config.headers)
        return resp

    def get_party(
            self,
            party_id: str = None,
            resolve_mode: str | ResolveMode = None,
            _user_doi: str = None
    ) -> str:
        doi_mode =resolve_mode

        if isinstance(doi_mode, ResolveMode):
            doi_mode = resolve_mode.value
        if doi_mode.lower() not in ["doi", "full"]:
            raise ValueError("Resolution mode must be either 'doi' or 'full'")

        endpoint = "party/resolve/"
        options = "?type={}".format(doi_mode)
        key = party_id

        if party_id is None:
            key = _user_doi
            endpoint = "user/resolve/"

        req = self.config.url + endpoint + key + options
        resp = requests.get(req, headers=self.config.headers)
        return resp.content.decode('utf-8')

    # https://registry1.eidr.org/EIDR/permissions/read/%7BassetID%7D?aclType={aclType
    # returns: An instance of the
        # eidr:AdminResponse or
        # eidr:PartyIDList

    def get_permissions(self, object_id: str, acl_type: str | ACL_Type):
        if isinstance(acl_type, ACL_Type):
            acl_type = acl_type.value
        req = self.config.url + 'permissions/read/' + object_id + '?aclType=' + acl_type
        resp = requests.get(req, headers=self.config.headers)
        return resp.content.decode('utf-8')

    def get_modification_base(self, object_id: str, mod_type: ModifyType | str):
        if isinstance(mod_type, ModifyType):
            mod_type = mod_type.value
        req = self.config.url + f'object/modificationbase/{object_id}/?type={mod_type}'
        resp = requests.get(req, headers=self.config.headers)
        return resp.content.decode('utf-8')

    def post(self, service: RegistryRequest):
        return self.post_raw(service.xml, service.name)

    def post_raw(self, xml: str, endpoint: str, params: dict = None):
        # multipart might be better off ignored here, assume it is always false for now
        if False:
            self.config.headers['Content-Type'] = f'multipart/form-data; boundary={self.config.boundary}'
        data = xml if True else (
            "{}\n{}\n{}\n{}\n{}\n{}".format(
                self.config.boundary,
                *[f'{k}: {v}' for k, v in params.items()],
                'Content-Disposition: form-data; name={}'.format(endpoint.split("/")[-1]),
                'Content-Transfer-Encoding: binary',
                xml,
                self.config.boundary
            ))
        # print(self.config.headers)
        # print(data)
        extra = ""
        if params is not None:
            for key, value in params.items():
                extra += "?{}={}".format(key, value)
        resp = requests.post(
            self.config.url + endpoint + "/" + extra,
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
    exp = Query.base_obj_expression(
        release_date="2005"
    )
    # print(exp)
    q = Query(
        expression=exp,
        page_num=1,
        page_size=1
    )

    res = driver.post(RegistryRequest(
        operations=[q]
    ))

    return to_pretty_xml(res.content)


def test_delete():
    driver = API_Driver.from_default()
    d = Delete(
        id="10.5240/55C4-C624-362D-B110-0F9D-J"
    )
    req = RegistryRequest(
        operations=[d]
    )
    print(req.xml)
    res = driver.post(req)

    return to_pretty_xml(res.content)


# print(test_delete())

def test_video_service_get():
    driver = API_Driver.from_default()
    res = driver.get_video_service("10.5239/170B-1D36", ResolveMode.FULL)
    print(res)

def test_permissions():
    driver = API_Driver.from_default()
    res = driver.get_permissions("10.5240/8B55-F9AA-007F-B18E-C000-6", ACL_Type.MODIFY)
    print(res)

if __name__ == "__main__":
    # test_post_file()
    # test_get()
    # test_query()
    # test_video_service_get()
    # test_permissions()
    pass
