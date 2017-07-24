import os
import argparse

DIR_NOT_EXIST = -1


def get_all_files(dir):
    path_f = []
    for dirs, subdirs, files in os.walk(dir):
        for f in files:
                path = os.path.join(dirs, f)
                path_f.append(path)
    return sorted(path_f, key=lambda file: os.path.basename(file))


def are_files_duplicates(file1, file2):
    return os.path.basename(file1) == os.path.basename(file2) and os.path.getsize(file1) == os.path.getsize(file2)


def is_dir_exist(dir):
    return os.path.exists(dir)


def find_duplicates(dir):
    duplicates = []
    path_f = get_all_files(dir)
    files_iterator = iter(path_f)
    next(files_iterator)
    try:
        for file in path_f:
            next_file = next(files_iterator)
            if are_files_duplicates(file, next_file):
                duplicates.append((file, next_file))
    except StopIteration:
        pass
    return duplicates


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("dirpath", type=str, help="Path to cheking dir")
    return parser.parse_args()


if __name__ == '__main__':
    if is_dir_exist(arg_parser().dirpath):
        duplicates = find_duplicates(arg_parser().dirpath)
        if duplicates:
            print("\n".join("{} дублируется с {}".format(duplicate[0], duplicate[1]) for duplicate in duplicates))
        else:
            print("Дубликатов нет")
    else:
        print("Такой директории не существует")