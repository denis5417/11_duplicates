import sys
import os


def get_all_files(dir):
    path_f = []
    for dirs, subdirs, files in os.walk(dir):
        for f in files:
            if not f.startswith("."):
                path = os.path.join(dirs, f)
                path_f.append(path)
    return path_f


def are_files_duplicates(file1, file2):
    return os.path.basename(file1) == os.path.basename(file2) and os.path.getsize(file1) == os.path.getsize(file2)


def find_duplicates(dir):
    if not os.path.exists(dir):
        print("Такой директории не существует")
        return None
    path_f = get_all_files(dir)
    for counter_1 in range(0, len(path_f)):
        for counter_2 in range(counter_1+1, len(path_f)):
            if are_files_duplicates(path_f[counter_1], path_f[counter_2]):
                    print("Файл {} дублируется с файлом {}".format(path_f[counter_2], path_f[counter_1]))


if __name__ == '__main__':
    try:
        find_duplicates(sys.argv[1])
    except IndexError:
        print("Укажите название файла")