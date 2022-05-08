from functools import reduce
import operator
from clean_files import utils
import filecmp
import os
from pathlib import Path


def get_files_same_content(path_X, paths_Y):
    files_X = utils.get_files_paths_from_dir(path_X)
    files_Y = set(
        reduce(
            operator.concat,
            map(utils.get_files_paths_from_dir, paths_Y),
        )
    )
    all_pairs = [
        (
            file_X,
            [
                file_Y
                for file_Y in files_Y
                if filecmp.cmp(file_X, file_Y)
            ],
        )
        for file_X in files_X
    ]
    return [
        (pair[0], pair[1]) for pair in all_pairs if len(pair[1]) > 0
    ]


def get_empty_files(path_X, paths_Y=None):
    files = utils.connect_paths_files(path_X=path_X, paths_Y=paths_Y)
    return [
        file_name
        for file_name in set(files)
        if os.stat(file_name).st_size == 0
    ]


def get_temp_files(path_X, paths_Y=None):
    files = utils.connect_paths_files(path_X=path_X, paths_Y=paths_Y)
    wrong_ext = utils.get_config_params()["temp_ext"]
    temp_files = []
    for file_path in files:
        for ext in wrong_ext:
            if str.endswith(str(file_path), ext):
                temp_files.append(file_path)
                break
    return temp_files


def get_same_name_files(path_X, paths_Y):
    files_X = utils.get_files_paths_from_dir(path_X)
    files_Y = list(
        set(
            reduce(
                operator.concat,
                map(utils.get_files_paths_from_dir, paths_Y),
            )
        )
    )
    all_pairs = [
        (
            file_X,
            [
                file_Y
                for file_Y in files_Y
                if os.path.basename(file_X) == os.path.basename(file_Y)
            ],
        )
        for file_X in files_X
    ]
    return [
        (pair[0], pair[1]) for pair in all_pairs if len(pair[1]) > 0
    ]


def get_wrong_permissions_files(path_X, paths_Y=None):
    files = utils.connect_paths_files(path_X=path_X, paths_Y=paths_Y)
    wrong_perms = utils.get_config_params()["weird_perms"]
    wrong_perm_files = []
    for file_path in files:
        for wrong_perm in wrong_perms:
            if (
                oct(os.stat(file_path).st_mode)[-3:]
                == "00{}".format(
                    oct(utils.to_mask(wrong_perm)).split("o")[-1]
                )[-3:]
            ):
                wrong_perm_files.append(file_path)
                break
    return wrong_perm_files


def get_wrong_signs_files(path_X, paths_Y=None):
    files = utils.connect_paths_files(path_X=path_X, paths_Y=paths_Y)
    wrong_signs = utils.get_config_params()["dang_chars"]
    wrong_sign_files = []
    for file_path in files:
        for wrong_sign in wrong_signs:
            if wrong_sign in Path(file_path).resolve().stem:
                wrong_sign_files.append(file_path)
                break
    return wrong_sign_files


def get_files_not_in_X(path_X, paths_Y):
    files_X = utils.get_files_paths_from_dir(path_X)
    files_Y = set(
        reduce(
            operator.concat,
            map(utils.get_files_paths_from_dir, paths_Y),
        )
    )
    files_new = []
    for file_Y in files_Y:
        is_file_new = True
        name_Y = os.path.basename(file_Y)
        for file_X in files_X:
            name_X = os.path.basename(file_X)
            if filecmp.cmp(file_X, file_Y) or name_X == name_Y:
                is_file_new = False
                break
        if is_file_new:
            files_new.append(file_Y)
    return files_new
