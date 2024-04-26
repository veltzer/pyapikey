import os
import os.path
import subprocess
from typing import Any
import datetime
import json


def old_get_key(domain: str) -> str:
    filename = os.path.expanduser("~/.config/pyapikey.json")
    with open(filename, "rt") as file_handle:
        keys = json.load(file_handle)
        return keys[domain]


def get_key(path: str) -> str:
    """
    Retrieves a password from the pass password manager.

    Args:
        path (str): The path to the password in the pass store.

    Returns:
        str: The password stored at the given path.

    Raises:
        Exception: If an error occurs while running the pass command.
    """
    cmd = ["pass", "show", f"keys/{path}"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as process:
        output, error = process.communicate()

    if process.returncode == 0:
        return output.decode().strip()
    raise ValueError(f"Error retrieving password: {error.decode()}")


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
    FILENAME = os.path.expanduser("~/.config/pyapikey.temp.json")

    def __init__(self):
        if os.path.isfile(TempStore.FILENAME):
            with open(TempStore.FILENAME) as file_handle:
                self.data = json.load(file_handle, object_hook=object_hook)
        else:
            self.data = {}

    def get(self, key: str) -> Any:
        return self.data[key]

    def set(self, key: str, value: Any) -> None:
        self.data[key] = value

    def has(self, key: str) -> bool:
        return key in self.data

    def save(self):
        dirname = os.path.dirname(TempStore.FILENAME)
        if not os.path.isdir(dirname):
            os.makedirs(dirname)
        with open(TempStore.FILENAME, "wt") as file_handle:
            json.dump(fp=file_handle, obj=self.data, default=default, indent=4)
