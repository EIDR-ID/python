from pathlib import Path
from venv import create

from app.scheme.org.eidr.schema import BaseObjectInfoType

import json
from enum import Enum, EnumType
from optparse import Option
from textwrap import dedent
from types import NoneType
from typing import Optional, Set, get_type_hints, get_origin, Union, get_args, List, Tuple, Any, Type, Dict
import re
from xml.etree.ElementTree import indent

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import JsonParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import JsonSerializer, DictFactory
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from urllib.parse import uses_params

from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.datatype import XmlDate, XmlPeriod, XmlDuration

import app.scheme.org.eidr.schema
from app.scheme.org.eidr.schema import SimpleInfo, ExtraObjectMetadataType, QueryType

from dataclasses import make_dataclass, field, fields, is_dataclass

from app.services import Query, ResponseReader
from app.driver import API_Driver

from app.scheme.org.eidr.schema import CreateBasicDataType, enum_mapping

import inspect

from app.scheme.org.eidr.schema import CreateEpisode, CreateEpisodeDataType


def attempt(func):
    """
    A Go-like attempt function that returns a tuple of the result and an exception if it occurs.
    :param func: function to attempt
    :return: tuple of (result, exception)
    """
    try:
        return func(), None
    except Exception as e:
        return None, e


def is_optional_type(t) -> bool:
    # Check if the type is a Union (which Optional is)
    if get_origin(t) is Union:
        args = get_args(t)
        # Check if one of the Union arguments is None
        return type(None) in args
    return False


def get_optional_inner_type(t):
    if is_optional_type(t):
        args = get_args(t)
        # Return the first non-None type (e.g., Optional[int] -> int)
        return next(a for a in args if a is not type(None))
    return None


def get_type_name(t: type) -> str:
    if get_origin(t) is Union:
        args = get_args(t)
        if len(args) == 2 and type(None) in args:
            inner = next(a for a in args if a is not type(None))
            return f"Optional[{get_type_name(inner)}]"
    return getattr(t, "__name__", str(t))


allowed_types: Set[type] = {
    str, int, float, bool, type(None), Enum, Optional[str], Optional[int], Optional[float],
    Optional[bool], Union[XmlPeriod, XmlDate, NoneType], XmlPeriod, XmlDate, XmlDuration
}


## Deprecated, use instance to Dict using a default instance of a class
def to_field_dict(cls, default_enums=True, include_xml=True) -> dict | str:
    hints = get_type_hints(cls)
    name = cls.__name__

    out = {}
    if is_dataclass(cls) and include_xml:
        out["_xml_"] = generate_xml(cls)
    if issubclass(cls, Enum):  # Handle enum case (only need a string out)
        out = list(cls)[0].value if default_enums else ""
    elif cls in allowed_types:
        return generate_default(cls)

    for member, _type in hints.items():
        # Happy case, no special handling needed
        if _type in allowed_types:
            # Preserve hinted types (i.e. Optional[str] instead of None or str)
            if is_optional_type(_type):
                inner_type = get_optional_inner_type(_type)
                out[member] = generate_default(inner_type)
                out[member + "_dataclass"] = inner_type
            else:
                out[member] = generate_default(_type)
                out[member + "_dataclass"] = _type
        else:
            if get_origin(_type) is list:
                inner_type = get_args(_type)[0]
                if inner_type not in allowed_types:
                    obj_dict = to_field_dict(inner_type, default_enums, include_xml)
                    out[member] = [obj_dict]
                else:
                    out[member] = []
                out[member + "_dataclass"] = List[inner_type]
            else:
                if is_optional_type(_type):
                    inner = to_field_dict(get_optional_inner_type(_type), default_enums, include_xml)
                    out[member + "_dataclass"] = _type
                else:
                    inner = to_field_dict(_type, default_enums, include_xml)
                out[member] = inner
                out[member + "_dataclass"] = _type

    return out


default_map: Dict[type, Any] = {
    XmlPeriod: "1999-10+03:30",
    XmlDate: "1970-01-01",
    XmlDuration: "P2Y6M5DT12H",
    int: 0,
    NoneType: None,
}


## Create an instance of a dataclass with default values, including for nested dataclasses
def default_dataclass(cls, default_enums=True):
    """
    Create an instance of a dataclass with default values, including for nested dataclasses.
    :param cls: The dataclass to create an instance of.
    :param default_enums: If True, use the first value of the enum as the default value.
    :return: An instance of the dataclass with default values.
    """
    if not is_dataclass(cls):
        raise TypeError(f"{cls} is not a dataclass")

    hints = get_type_hints(cls)
    params = {}
    for name, _type in hints.items():
        if get_origin(_type) is not list:
            _type = extract_union(_type)
            if _type in default_map:
                params[name] = default_map[_type]
            elif is_dataclass(_type):
                inner = default_dataclass(_type)
                params[name] = inner
            elif issubclass(_type, Enum):
                params[name] = list(_type)[0].value if default_enums else ""
            else:
                params[name] = _type()
        else:  # Make a list containing a single default value
            inner_type = get_args(_type)[0]
            val = None
            if inner_type in default_map:
                val = default_map[inner_type]
            elif is_dataclass(inner_type):
                val = default_dataclass(inner_type)
            elif issubclass(inner_type, Enum):
                val = list(inner_type)[0].value if default_enums else ""
            else:
                val = _type()
            params[name] = [val]
    out = cls(**params)
    return out


def extract_union(t):
    if get_origin(t) is Union:
        args = get_args(t)
        if len(args) >= 2 and type(None) in args:
            return next(a for a in args if a is not type(None))  # gets the first non-None type
        return None
    else:
        return t


def generate_default(cls):
    sig = inspect.signature(cls.__init__)
    if len(sig.parameters) == 0:
        return cls()
    if cls in default_map:
        return cls(default_map[cls])
    return cls("")


serializer = XmlSerializer(config=SerializerConfig(indent="     ", xml_declaration=True))
ns_map = {
    "": "http://www.eidr.org/schema",
    "MOVIELABS": "http://www.movielabs.com/schema/md/v2.8/md"
}
composite_ns = {
    "EIDR": "http://www.eidr.org/schema",
    "MOVIELABS": "http://www.movielabs.com/schema/md/v2.8/md",
}


def generate_xml(cls):
    global serializer, ns_map, composite_ns
    if not is_dataclass(cls):
        raise TypeError(f"{cls} is not a dataclass")
    if not hasattr(cls.Meta, "namespace") or cls.Meta.namespace != "http://www.eidr.org/schema":
        xml_str = serializer.render(cls, composite_ns)
    else:
        xml_str = serializer.render(cls, ns_map)
    return xml_str


def filter_type_info(d: dict, substr: str = "_dataclass"):
    out = {}
    for key, value in d.items():
        if isinstance(value, dict):
            out[key] = filter_type_info(value, substr)
        elif isinstance(value, list):
            out[key] = []
            for item in value:
                if isinstance(item, dict):
                    out[key].append(filter_type_info(item, substr))
                else:
                    out[key].append(item)
        elif substr not in key:
            out[key] = value

    return out


non_serials = {XmlPeriod, XmlDate, XmlDuration}


def repr_non_serials(d: dict):
    out = {}
    for key, value in d.items():
        if isinstance(value, dict):
            out[key] = repr_non_serials(value)
        elif isinstance(value, list):
            out[key] = []
            for item in value:
                if isinstance(item, dict):
                    out[key].append(repr_non_serials(item))
                else:
                    out[key].append(item)
        elif type(value) in non_serials:
            out[key] = str(value)
        else:
            out[key] = value

    return out


context = XmlContext()
json_serializer = JsonSerializer(config=SerializerConfig(xml_declaration=True))
json_parser = JsonParser(config=ParserConfig(base_url="http://www.eidr.org/schema", process_xinclude=True), context=())


def instance_to_dict(obj, include_type: bool = False) -> Dict:
    """
    Convert a dataclass to a dict representation.
    :param obj: dataclass instance
    :return:
        dict representation of the dataclass
    """
    global json_serializer
    if not is_dataclass(obj):
        raise TypeError(f"{obj} is not a dataclass")
    dict_out = json.loads(json_serializer.render(obj))
    if include_type:
        dict_out["_dataclass"] = type(obj)
    return dict_out


def dict_to_instance(d: Dict, t: Type = None) -> Any:
    """
    Convert a dict representation of a dataclass to an instance of the dataclass.
    :param d: dict representation of the dataclass
    :return:
        instance of the dataclass
    """
    global json_parser
    if not isinstance(d, dict):
        raise TypeError(f"{d} is not a dict")
    if t is not None:
        return json_parser.from_string(json.dumps(d), t)
    elif "_dataclass" not in d:
        return json_parser.from_string(json.dumps(d))
    else:
        copy = d.copy()
        del copy["_dataclass"]
        return json_parser.from_string(json.dumps(copy), d["_dataclass"])


def generate_templates(directory: Path, class_types: List[Enum]):
    """
    Generate json template files for record construction and other operations.
    :param directory: the directory to generate the files in
    :param class_types: Dataclass types intended to be generated.
    :return:
    """
    if not directory.exists():
        directory.mkdir(parents=True, exist_ok=True)
    for clazz in class_types:
        d = instance_to_dict(default_dataclass(enum_mapping.get(clazz, None)))
        file_name = clazz.name.lower() + ".json"
        file_path = directory / file_name
        try:
            with open(file_path, "x") as f:
                f.write(json.dumps(d, indent=4))
        except FileExistsError:
            print(f"The file {file_name} already exists")
        except Exception as e:
            print(f"An unexpected error occurred while trying to generate a template"
                  f"file for dataclass {file_name}: {e}")


def from_json(file_path: Path):
    """
    Read a json file and convert it to a dictionary.
    :param file_path: the path to the json file
    :return:
        dict: dict representation of the json file
    """
    if not isinstance(file_path, Path):
        raise TypeError(f"{file_path} is not a Path")
    elif not file_path.exists():
        raise FileNotFoundError(f"{file_path} does not exist")
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"The file you're trying to access '{file_path}', does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred while reading the file '{file_path}': {e}")


if __name__ == "__main__":  # TODO: Move to test file
    # Test the RegistryHandler
    # Example usage
    # indents = 4
    # out = to_field_dict(QueryType)
    # out = default_dataclass(QueryType)
    # print(out)

    # testing default dataclass
    default = default_dataclass(CreateBasicDataType)
    out = instance_to_dict(default_dataclass(CreateBasicDataType))
    reverse = dict_to_instance(out)
    print(reverse)
