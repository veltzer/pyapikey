import os
from typing import Any
import datetime
import json


def get_key(domain: str) -> str:
    filename = os.path.expanduser("~/.config/pyapikey.json")
    with open(filename, "rt") as file_handle:
        keys = json.load(file_handle)
        return keys[domain]


def default(obj):
    if isinstance(obj, datetime.datetime):
        return {'_isoformat': obj.isoformat()}
    return str(obj)


def object_hook(obj):
    _isoformat = obj.get('_isoformat')
    if _isoformat is not None:
        return datetime.datetime.fromisoformat(_isoformat)
    return obj


class TempStore:
    def __init__(self):
        filename = os.path.expanduser("~/.config/pyapikey.temp.json")
        if os.path.isfile(filename):
            with open(filename) as file_handle:
                self.data = json.load(file_handle, object_hook=object_hook)
        else:
            self.data = {}

    def get(self, key: str) -> Any:
        return self.data[key]

    def set(self, key: str, value: Any) -> None:
        self.data[key] = value

    def save(self):
        filename = os.path.expanduser("~/.config/pyapikey.temp.json")
        with open(filename, 'w') as file_handle:
            json.dump(fp=file_handle, obj=self.data, default=default)
