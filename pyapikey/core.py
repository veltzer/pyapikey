import os
import json
from typing import Any


def get_key(domain: str) -> str:
    filename = os.path.expanduser("~/.config/pyapikey.json")
    with open(filename, "rt") as file_handle:
        keys = json.load(file_handle)
        return keys[domain]


class TempStore:
    def __init__(self):
        filename = os.path.expanduser("~/.config/pyapikey.temp.json")
        with open(filename) as file_handle:
            self.data = json.load(file_handle)

    def get(self, key: str) -> Any:
        return self.data[key]

    def set(self, key: str, value: Any) -> None:
        self.data[key] = value

    def save(self):
        filename = os.path.expanduser("~/.config/pyapikey.temp.json")
        with open(filename, 'w') as file_handle:
            json.dump(self.data, file_handle, indent=4)
