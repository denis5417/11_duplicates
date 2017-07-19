import sys
import os


def delete_duplicates(dir):
    if not os.path.exists(dir):
        print("Такой директории не существует")
        return None
    path_f = []
    for dirs, subdirs, files in os.walk(dir):
        for f in files:
            if not f.startswith("."):
                path = os.path.join(dirs, f)
                path_f.append(path)
    for counter_1 in range(0, len(path_f)):
        for counter_2 in range(counter_1+1, len(path_f)):
            if os.path.basename(path_f[counter_1]) == os.path.basename(path_f[counter_2]) \
                        and os.path.getsize(path_f[counter_1]) == os.path.getsize(path_f[counter_2]):
                    print("Файл {} дублируется с файлом {}".format(path_f[counter_2], path_f[counter_1]))


if __name__ == '__main__':
    delete_duplicates(sys.argv[1])
