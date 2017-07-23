import os
import argparse
from time import time

DIR_NOT_EXIST = -1

def get_all_files(dir):
    path_f = []
    for dirs, subdirs, files in os.walk(dir):
        for f in files:
            if not f.startswith("."):
                path = os.path.join(dirs, f)
                path_f.append(path)
    return sorted(path_f, key=lambda file: os.path.basename(file))


def are_files_duplicates(file1, file2):
    return os.path.basename(file1) == os.path.basename(file2) and os.path.getsize(file1) == os.path.getsize(file2)


def find_duplicates(dir):
    duplicates = []
    if not os.path.exists(dir):
        return DIR_NOT_EXIST
    path_f = get_all_files(dir)
    for counter in range(0, len(path_f)-1):
        if are_files_duplicates(path_f[counter], path_f[counter + 1]):
                duplicates.append((path_f[counter], path_f[counter + 1]))
    return duplicates


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("dirpath", type=str, help="Path to cheking dir")
    return parser.parse_args()


if __name__ == '__main__':
    duplicates = find_duplicates(arg_parser().dirpath)
    if duplicates == -1:
        print("Такой директории не существует")
    elif duplicates:
        print("\n".join("{} дублируется с {}".format(duplicate[0], duplicate[1]) for duplicate in duplicates))
    else:
        print("Дубликатов нет")