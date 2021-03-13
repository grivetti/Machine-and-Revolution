import pickle
from typing import Union, Dict
from re import sub

def read_file(file: str) -> Union[str, Dict]:
    with open(file, "rb") as filedb:
        db = pickle.load(filedb)
        for keys in db:
            yield keys, db[keys]

def sepate_uppercase(name: str) -> str:
    name = sub( r"([A-Z])", r" \1", name).split()
    return " ".join(name)