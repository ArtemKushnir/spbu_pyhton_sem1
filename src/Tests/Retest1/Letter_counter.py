from os.path import exists
import re
import sys
from collections import Counter


def get_text(file_name):
    with open(file_name) as read_file:
        reg = re.compile('[^a-zA-Z]')
        return reg.sub('', str(read_file.readlines()))


def count_letters(text):
    text = Counter(list(text))
    result = dict(sorted(text.items()))
    return result


def write_in_file(file_name, result):
    with open(file_name, "w") as write_file:
        for key in result:
            write_file.write(f"{key}: {result[key]}\n")


def file_check(read_file_name, write_file_name):
    if not (exists(read_file_name)):
        print(f"не существует {read_file_name}")
        return False
    if exists(write_file_name):
        print(f"файл {write_file_name} уже существует")
        return False
    return True


def main():
    read_file_name, write_file_name = sys.argv[1:]
    if file_check(read_file_name, write_file_name):
        read_file_chars = get_text(read_file_name)
        result_dict_chars = count_letters(read_file_chars)
        write_in_file(write_file_name, result_dict_chars)


if __name__ == "__main__":
    main()