import argparse
import os
from clean_files import interface


def check_path_exists(path):
    return os.path.exists(path)


def check_path_args(path_X, paths_Y=[]):
    if not check_path_exists(path_X):
        print("Given path X does not exists!")
        return False
    if len(paths_Y) != 0 and not any(map(check_path_exists, paths_Y)):
        print("Given path Y does not exists!")
        return False
    if len(paths_Y) != 0 and path_X in paths_Y:
        print("One of paths in Y are same as path X!")
        return False
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Linux directory organizer"
    )
    parser.add_argument("-X", type=str, help="path to X directory")
    parser.add_argument("-Y", nargs="*", default=[])
    args = parser.parse_args()
    if check_path_args(path_X=args.X, paths_Y=args.Y):
        interface.main(path_X=args.X, paths_Y=args.Y)
