import hashlib
import json
from functools import reduce
import operator
import os
from pathlib import Path


def to_mask(rights_str):
    assert type(rights_str) is str
    assert len(rights_str) == 9
    mask = "".join(map(lambda x: "0" if x == "-" else "1", rights_str))
    return int(mask, 2)


def are_files_same_content(file1, file2):
    return (
        hashlib.md5(file1).hexdigest() == hashlib.md5(file2).hexdigest()
    )


def get_config_params():
    with open("clean_files.json", "r") as f:
        config = json.load(f)
    return config


def connect_paths_files(path_X, paths_Y):
    files_X = get_files_paths_from_dir(path_X)
    if paths_Y:
        files_Y = list(
            set(
                reduce(
                    operator.concat,
                    map(get_files_paths_from_dir, paths_Y),
                )
            )
        )
        files_X.extend(files_Y)
        files_X = set(files_X)
    return files_X


def get_files_paths_from_dir(dir_path):
    files = []
    for r, _, f in os.walk(dir_path):
        files.extend(
            [
                Path(os.path.join(r, file_name)).resolve()
                for file_name in f
            ]
        )
    return files
