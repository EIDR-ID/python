from pathlib import Path
from venv import create

from app.scheme.org.eidr.schema import BaseObjectInfoType, CreationType

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
from xsdata.models.datatype import XmlDate, XmlPeriod, XmlDuration, XmlTime

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
    XmlTime: "12:00:00",
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


TemplateType = CreationType


def _get_creation_name(t: TemplateType) -> str:
    """
    Get the name of the creation type from the object. Quick and dirty helper function.
    :param t: The type to get the name from.
    :return: The name of the creation type.
    """
    return t.name.replace("CREATE_", "").title()


def split_list(arr: list, i: int) -> (list, list):
    return arr[:i], arr[i:]


def fill_dict(d: dict, fill: dict) -> dict:
    """
    Fill a dictionary with values from another dictionary. Keep the structure and unvistied values of the first dictionary.
    :param d: The dictionary to fill.
    :param fill: The dictionary with values to fill in.
    :return: The filled dictionary.
    """
    out = d.copy()
    for key, value in out.items():
        if key not in fill:
            continue
        if isinstance(value, dict):
            out[key] = fill_dict(value, fill[key])
        elif isinstance(value, list):
            if len(fill[key]) == 0:
                out[key] = []
                continue

            original = value.copy()
            modified, new = split_list(fill[key], len(original))
            for i in range(len(original)):
                item, change = original[i], modified[i]
                if isinstance(item, dict):
                    original[i] = fill_dict(item, change)
                else:
                    out[key].append(change)

            # if key in fill and len(fill[key]) == 0:
            #     d[key] = []
            #     continue
            # for i in range(len(vals)):
            #     if isinstance(vals[i], dict):
            #         if key in fill and i < len(fill[key]):
            #             value[i] = fill_dict(value[i], fill[key][i])
            #         else:
            #             value[i] = fill_dict(value[i], {})
        elif key in fill:
            d[key] = fill[key]
    return d


def generate_template_fill(t: TemplateType, merges: List[Dict[str, Any]]) -> Dict[str, Any]:
    d = instance_to_dict(default_dataclass(enum_mapping.get(t, None)))
    d["BaseObjectData"]["ReferentType"] = _get_creation_name(t)
    for merge in merges:
        d = merge_dicts(d, merge)
    return d
def generate_templates(directory: Path, class_types: List[TemplateType | Enum],
                       fill: List[Dict[str, Any] | None] = None):
    """
    Generate json template files for record construction and other operations.
    :param fill:
    :param directory: the directory to generate the files in
    :param class_types: Dataclass types intended to be generated.
    :return:
    """
    if not directory.exists():
        directory.mkdir(parents=True, exist_ok=True)

    for i, clazz in enumerate(class_types):
        d = instance_to_dict(default_dataclass(enum_mapping.get(clazz, None)))
        file_name = clazz.name.lower() + ".json"
        file_path = directory / file_name

        if fill and len(fill) - 1 >= i and fill[i]:
            d = remove_nulls(merge_dicts(d, fill[i]))
        d["BaseObjectData"]["ReferentType"] = _get_creation_name(clazz)
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


def _deep_merge(original: Any, diff: Any) -> Any:
    """
    Merge *diff* into *original* according to custom rules:

    • Keys that appear only in *diff* are ignored.
    • Scalars or mismatched types → replace original with diff.
    • Dict ∩ Dict           → recurse key-by-key (only on keys present in *original*).
    • List ∩ List           → walk indices:
        – if both values are dicts → recurse extra_info, only with keys that exist in original
        – otherwise replace element with diff’s element
        – append any extra tail elements from diff
    """
    # --- both dictionaries --------------------------------------------------
    if isinstance(original, dict) and isinstance(diff, dict):
        merged: Dict[str, Any] = {}
        for k, ov in original.items():  # only iterate original keys
            if k in diff:  # key exists in both → extra_info
                merged[k] = _deep_merge(ov, diff[k])
            else:  # key only in original → keep
                merged[k] = ov
        return merged

    # --- both lists ----------------------------------------------------------
    if isinstance(original, list) and isinstance(diff, list):
        if len(diff) == 0:
            return []
        merged_list: List[Any] = []
        common_len = min(len(original), len(diff))

        # replace / recurse for shared indices
        for i in range(common_len):
            # Only extra_info if both elements are dictionaries
            if isinstance(original[i], dict) and isinstance(diff[i], dict):
                # Merge dicts but only keep keys from original
                merged_list.append(_deep_merge(original[i], {k: diff[i][k] for k in original[i] if k in diff[i]}))
            else:
                # Otherwise, replace element with diff's element
                merged_list.append(diff[i])

        # keep any leftover items from original if diff is shorter
        if len(original) > common_len:
            merged_list.extend(original[common_len:])

        # append any excess items from diff if diff is longer
        if len(diff) > common_len:
            merged_list.extend(diff[common_len:])

        return merged_list

    # --- scalar or mismatched types -----------------------------------------
    if isinstance(original, type(diff)):
        return diff  # replace outright if types match
    elif original is not None and diff is None:
        return None  # allow removal
    else:
        return original  # keep original if diff has the wrong type


def merge_dicts(original: Dict[str, Any], diff: Dict[str, Any]) -> Dict[str, Any]:
    """Public helper that enforces top-level dict types."""
    if not (isinstance(original, dict) and isinstance(diff, dict)):
        raise TypeError("Both arguments must be dictionaries")
    out = _deep_merge(original, diff)

    return _deep_merge(original, diff)


def _remove_null(o: any):
    if isinstance(o, dict):
        for key, value in list(o.items()):
            if value is None:
                del o[key]
            else:
                _remove_null(value)
    elif isinstance(o, list):
        new_list = [item for item in o if item is not None]
        for item in new_list:
            if isinstance(item, dict):
                _remove_null(item)
        return new_list
    return o


def remove_nulls(d: dict) -> dict:
    """
    Remove all None values from a dictionary.
    :param d: The dictionary to remove None values from.
    :return: The dictionary without None values.
    """
    return _remove_null(d)



if __name__ == "__main__":  # TODO: Move to test file
    # Test the RegistryHandler
    # Example usage
    # indents = 4
    # out = to_field_dict(QueryType)
    # out = default_dataclass(QueryType)
    # print(out)

    # testing default dataclass
    # default = default_dataclass(CreateBasicDataType)
    # out = instance_to_dict(default_dataclass(CreateBasicDataType))
    # reverse = dict_to_instance(out)
    # print(reverse)
    print(merge_dicts({"a": 1, "b": {"c": [{"d": 21}]}}, {"b": {"c": [{"d": 21}, {"e": 22}]}}))
