import os
from clean_files import utils
from pathlib import Path
import re


def remove_file(file_path):
    assert os.path.exists(file_path) is True
    os.remove(file_path)


def apply_all(func, list_args, extra_const_arg=None):
    if len(list_args) != 0:
        for arg in list_args:
            func(arg, extra_const_arg) if extra_const_arg else func(arg)


def move_file(path_from, path_to):
    assert os.path.exists(path=path_from) is True
    os.replace(path_from, path_to)


def change_older_to_newer(files):
    file_X = files[0]
    files_Y = files[1]
    files_Y_sorted = sorted(files_Y, key=lambda p: -os.stat(p).st_mtime)
    if os.stat(file_X).st_mtime < os.stat(files_Y_sorted[0]).st_mtime:
        new_path = os.path.join(
            file_X.parent, os.path.basename(files_Y_sorted[0])
        )
        remove_file(file_X)
        move_file(path_from=files_Y_sorted[0], path_to=new_path)
        files_Y_sorted.pop(0)
    apply_all(remove_file, files_Y_sorted)


def change_newer_to_older(files):
    file_X = files[0]
    files_Y = files[1]
    files_Y_sorted = sorted(files_Y, key=lambda p: os.stat(p).st_mtime)
    if os.stat(file_X).st_mtime > os.stat(files_Y_sorted[0]).st_mtime:
        new_path = os.path.join(
            file_X.parent, os.path.basename(files_Y_sorted[0])
        )
        remove_file(file_X)
        move_file(path_from=files_Y_sorted[0], path_to=new_path)
        files_Y_sorted.pop(0)
    apply_all(remove_file, files_Y_sorted)


def move_to_directory(file_path, directory_path):
    new_file_path = os.path.join(
        directory_path, os.path.basename(file_path)
    )
    move_file(path_from=file_path, path_to=new_file_path)


def change_file_attributes(file_path, new_perm=None):
    if new_perm is None:
        new_perm = utils.get_config_params()["default_perm"]
    file_path.chmod(utils.to_mask(new_perm))


def change_file_name(file_path, new_file_name=None):
    path_of_file = Path(file_path).resolve()
    if new_file_name:
        new_file_name = Path(new_file_name).resolve()
        file_name, file_ext = new_file_name.stem, new_file_name.suffix
    else:
        file_name, file_ext = path_of_file.stem, path_of_file.suffix
    sub_char = utils.get_config_params()["default_char"]
    for ch in utils.get_config_params()["dang_chars"]:
        print(file_name + " " + ch)
        file_name = re.sub(ch, sub_char, file_name)
    print(file_name)
    os.rename(
        file_path,
        os.path.join("./", path_of_file.parent, file_name + file_ext),
    )
