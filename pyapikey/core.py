import os
import json


def get_key(domain: str) -> str:
    filename = os.path.expanduser("~/.config/pyapikey.json")
    with open(filename, "rt") as f:
        keys = json.load(f)
        return keys[domain]
