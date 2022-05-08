from importlib.resources import path
from clean_files import find_files, action_files


def handle_options(options, n_of_tabs=2):
    tabs = "\t" * n_of_tabs
    while True:
        try:
            usr_input = int(input(tabs + "Action: "))
        except ValueError:
            print("\t\tError|Should be number!")
            continue
        if usr_input in (options):
            break
        print("\t\tError|Should be correct option!")
    return usr_input


def handle_new_perm():
    while True:
        usr_input = input(
            "\t\tNew perimissions (only 'r', 'w', 'x' and '-'"
            " allowed): "
        )
        if len(usr_input) != 9:
            print("\t\tError|Should be string with a length of 9!")
            continue
        has_wrong_ch = False
        for ch in usr_input:
            if ch not in {"r", "w", "x", "-"}:
                print("\t\tError|Only 'r', 'w', 'x' and '-' allowed!")
                has_wrong_ch = True
                break
        if not has_wrong_ch:
            break
    return usr_input


def handle_new_name():
    while True:
        usr_input = input("\t\tNew name: ")
        if len(usr_input) != 0:
            break
        print("\t\tError|Pass name file!")
    return usr_input


def handle_said_all():
    while True:
        is_to_all_ans = input("\t\tApply to all? [y/n]: ")
        if is_to_all_ans in ({"y", "n"}):
            break
        print("\t\tError|Pass 'y' or 'n'!")
    is_to_all = True if is_to_all_ans == "y" else False
    return is_to_all


def print_hello():
    s = "Welcome to Unix files and directories organizer!\n"
    len_s = len(s)
    s += "~" * len_s
    print(s)


def print_finds_types(is_Y_provided):
    """
    Function prints user interface
    """
    if is_Y_provided:
        s = (
            "Choose what to find:\n"
            "1 -> MISSING FILES IN X\n"
            "2 -> FILES WITH SAME CONTENT\n"
            "3 -> EMPTY FILES\n"
            "4 -> FILES WITH SAME NAME\n"
            "5 -> TEMPORARY FILES\n"
            "6 -> FILES WITH UNUSUAL ATTRIBUTES\n"
            "7 -> FILES WITH TROUBLE CHARACTERS\n"
            "8 -> EXIT"
        )
    else:
        s = (
            "Choose what to find:\n"
            "1 -> EMPTY FILES\n"
            "2 -> TEMPORARY FILES\n"
            "3 -> FILES WITH UNUSUAL ATTRIBUTES\n"
            "4 -> FILES WITH TROUBLE CHARACTERS\n"
            "5 -> EXIT"
        )
    print(s)


def perform_missing(path_X, paths_Y=[]):
    if len(paths_Y) == 0:
        raise Exception("Not files Y provided!")
    files = find_files.get_files_not_in_X(
        path_X=path_X, paths_Y=paths_Y
    )
    is_said_all = False
    is_to_all = False
    for file in files:
        print(
            f"\tChoose what to do with {file}:\n"
            + "\t1 -> MOVE TO X\n"
            + "\t2 -> REMOVE\n"
            + "\t3 -> NOTHING"
        )
        usr_input = handle_options({1, 2, 3})
        if not is_said_all:
            is_to_all = handle_said_all()
            is_said_all = True
        if usr_input == 1:
            if is_to_all:
                action_files.apply_all(
                    action_files.move_to_directory, files, path_X
                )
                break
            else:
                action_files.move_to_directory(
                    file_path=file, directory_path=path_X
                )
        elif usr_input == 2:
            if is_to_all:
                action_files.apply_all(action_files.remove_file, files)
                break
            else:
                action_files.remove_file(file)
        elif usr_input == 3:
            if is_to_all:
                break
        else:
            raise Exception("Wrong argument as action!")


def perform_files_same_content(path_X, paths_Y=[]):
    if len(paths_Y) == 0:
        raise Exception("Not files Y provided!")
    files = find_files.get_files_same_content(
        path_X=path_X, paths_Y=paths_Y
    )
    is_said_all = False
    is_to_all = False
    for file_X, files_Y in files:
        n_of_Y = len(files_Y)
        print(
            f"\tChoose what to do with {file_X} which has"
            f" {n_of_Y} copies in Y:\n"
            + "\t1 -> REPLACE X WITH NEWEST AND REMOVE ALL COPIES\n"
            + "\t2 -> REPLACE X WITH OLDEST AND REMOVE ALL COPIES\n"
            + "\t3 -> REMOVE ALL COPIES\n"
            + "\t4 -> NOTHING"
        )
        usr_input = handle_options({1, 2, 3, 4})
        if not is_said_all:
            is_to_all = handle_said_all()
            is_said_all = True
        if usr_input == 1:
            if is_to_all:
                action_files.apply_all(
                    action_files.change_older_to_newer, files
                )
                break
            else:
                action_files.change_older_to_newer(
                    files=(file_X, files_Y)
                )
        elif usr_input == 2:
            if is_to_all:
                action_files.apply_all(
                    action_files.change_newer_to_older, files
                )
                break
            else:
                action_files.change_newer_to_older(
                    files=(file_X, files_Y)
                )
        elif usr_input == 3:
            if is_to_all:
                all_Y = sum([f[1] for f in files], [])
                action_files.apply_all(action_files.remove_file, all_Y)
                break
            else:
                action_files.apply_all(
                    action_files.remove_file, files_Y
                )
        elif usr_input == 4:
            if is_to_all:
                break
        else:
            raise Exception("Wrong argument as action!")


def perform_empty_files(path_X, paths_Y=[]):
    files = find_files.get_empty_files(path_X=path_X, paths_Y=paths_Y)
    is_said_all = False
    is_to_all = False
    for file in files:
        print(
            f"\tChoose what to do with {file}:\n"
            + "\t1 -> REMOVE\n"
            + "\t2 -> NOTHING"
        )
        usr_input = handle_options({1, 2})
        if not is_said_all:
            is_to_all = handle_said_all()
            is_said_all = True
        if usr_input == 1:
            if is_to_all:
                action_files.apply_all(action_files.remove_file, files)
                break
            else:
                action_files.remove_file(file_path=file)
        elif usr_input == 2:
            if is_to_all:
                break
        else:
            raise Exception("Wrong argument as action!")


def perform_same_name_files(path_X, paths_Y=[]):
    if len(paths_Y) == 0:
        raise Exception("Not files Y provided!")
    files = find_files.get_same_name_files(
        path_X=path_X, paths_Y=paths_Y
    )
    is_said_all = False
    is_to_all = False
    for file_X, files_Y in files:
        n_of_Y = len(files_Y)
        print(
            f"\tChoose what to do with {file_X} which has"
            f" {n_of_Y} files with same name in Y:\n"
            + "\t1 -> REPLACE X WITH NEWEST AND REMOVE ALL COPIES\n"
            + "\t2 -> REPLACE X WITH OLDEST AND REMOVE ALL COPIES\n"
            + "\t3 -> REMOVE ALL COPIES\n"
            + "\t4 -> NOTHING"
        )
        usr_input = handle_options({1, 2, 3, 4})
        if not is_said_all:
            is_to_all = handle_said_all()
            is_said_all = True
        if usr_input == 1:
            if is_to_all:
                action_files.apply_all(
                    action_files.change_older_to_newer, files
                )
                break
            else:
                action_files.change_older_to_newer(
                    files=(file_X, files_Y)
                )
        elif usr_input == 2:
            if is_to_all:
                action_files.apply_all(
                    action_files.change_newer_to_older, files
                )
                break
            else:
                action_files.change_newer_to_older(
                    files=(file_X, files_Y)
                )
        elif usr_input == 3:
            if is_to_all:
                all_Y = sum([f[1] for f in files], [])
                action_files.apply_all(action_files.remove_file, all_Y)
                break
            else:
                action_files.apply_all(
                    action_files.remove_file, files_Y
                )
        elif usr_input == 4:
            if is_to_all:
                break
        else:
            raise Exception("Wrong argument as action!")


def perform_temp_files(path_X, paths_Y=[]):
    files = find_files.get_temp_files(path_X=path_X, paths_Y=paths_Y)
    is_said_all = False
    is_to_all = False
    for file in files:
        print(
            f"\tChoose what to do with {file}:\n"
            + "\t1 -> REMOVE\n"
            + "\t2 -> CHANGE NAME\n"
            + "\t3 -> NOTHING"
        )
        usr_input = handle_options({1, 2, 3})
        if not is_said_all and usr_input != 2:
            is_to_all = handle_said_all()
            is_said_all = True
        if usr_input == 1:
            if is_to_all:
                action_files.apply_all(action_files.remove_file, files)
                break
            else:
                action_files.remove_file(file_path=file)
        elif usr_input == 2:
            new_file_name = handle_new_name()
            action_files.change_file_name(
                file_path=file, new_file_name=new_file_name
            )
        elif usr_input == 3:
            if is_to_all:
                break
        else:
            raise Exception("Wrong argument as action!")


def perform_wrong_attributes(path_X, paths_Y=[]):
    files = find_files.get_wrong_permissions_files(
        path_X=path_X, paths_Y=paths_Y
    )
    is_said_all = False
    is_to_all = False
    for file in files:
        print(
            f"\tChoose what to do with {file}:\n"
            + "\t1 -> REMOVE\n"
            + "\t2 -> CHANGE PERMISSIONS TO OWN\n"
            + "\t3 -> CHANGE PERMISSIONS TO DEFAULT\n"
            + "\t4 -> NOTHING"
        )
        usr_input = handle_options({1, 2, 3, 4})
        if not is_said_all:
            is_to_all = handle_said_all()
            is_said_all = True
        if usr_input == 1:
            if is_to_all:
                action_files.apply_all(action_files.remove_file, files)
                break
            else:
                action_files.remove_file(file_path=file)
        elif usr_input == 2:
            new_attr = handle_new_perm()
            if is_to_all:
                action_files.apply_all(
                    action_files.change_file_attributes, files, new_attr
                )
                break
            action_files.change_file_attributes(file, new_perm=new_attr)
        elif usr_input == 3:
            if is_to_all:
                action_files.apply_all(
                    action_files.change_file_attributes, files
                )
                break
            action_files.change_file_attributes(file)
        elif usr_input == 4:
            if is_to_all:
                break
        else:
            raise Exception("Wrong argument as action!")


def perform_wrong_name(path_X, paths_Y=[]):
    files = find_files.get_wrong_signs_files(
        path_X=path_X, paths_Y=paths_Y
    )
    is_said_all = False
    is_to_all = False
    for file in files:
        print(
            f"\tChoose what to do with {file}:\n"
            + "\t1 -> REMOVE\n"
            + "\t2 -> CHANGE NAME\n"
            + "\t3 -> CORRECT NAME\n"
            + "\t4 -> NOTHING"
        )
        usr_input = handle_options({1, 2, 3, 4})
        if not is_said_all and usr_input != 2:
            is_to_all = handle_said_all()
            is_said_all = True
        if usr_input == 1:
            if is_to_all:
                action_files.apply_all(action_files.remove_file, files)
                break
            else:
                action_files.remove_file(file_path=file)
        elif usr_input == 2:
            new_file_name = handle_new_name()
            action_files.change_file_name(
                file_path=file, new_file_name=new_file_name
            )
        elif usr_input == 3:
            if is_to_all:
                action_files.apply_all(
                    action_files.change_file_name, files
                )
                break
            action_files.change_file_name(file)
        elif usr_input == 4:
            if is_to_all:
                break
        else:
            raise Exception("Wrong argument as action!")


def main_only_X(path_X):
    while True:
        print_finds_types(is_Y_provided=False)
        usr_input = handle_options({1, 2, 3, 4, 5}, n_of_tabs=1)
        if usr_input == 1:
            perform_empty_files(path_X=path_X)
        elif usr_input == 2:
            perform_temp_files(path_X=path_X)
        elif usr_input == 3:
            perform_wrong_attributes(path_X=path_X)
        elif usr_input == 4:
            perform_wrong_name(path_X=path_X)
        elif usr_input == 5:
            break
        else:
            raise Exception("Wrong argument as action!")


def main_with_Y(path_X, paths_Y):
    while True:
        print_finds_types(is_Y_provided=True)
        usr_input = handle_options(
            {1, 2, 3, 4, 5, 6, 7, 8}, n_of_tabs=1
        )
        if usr_input == 1:
            perform_missing(path_X=path_X, paths_Y=paths_Y)
        elif usr_input == 2:
            perform_files_same_content(path_X=path_X, paths_Y=paths_Y)
        elif usr_input == 3:
            perform_empty_files(path_X=path_X, paths_Y=paths_Y)
        elif usr_input == 4:
            perform_same_name_files(path_X=path_X, paths_Y=paths_Y)
        elif usr_input == 5:
            perform_temp_files(path_X=path_X, paths_Y=paths_Y)
        elif usr_input == 6:
            perform_wrong_attributes(path_X=path_X, paths_Y=paths_Y)
        elif usr_input == 7:
            perform_wrong_name(path_X=path_X, paths_Y=paths_Y)
        elif usr_input == 8:
            break
        else:
            raise Exception("Wrong argument as action!")


def main(path_X, paths_Y=[]):
    print_hello()
    if len(paths_Y) == 0:
        main_only_X(path_X=path_X)
    else:
        main_with_Y(path_X=path_X, paths_Y=paths_Y)
