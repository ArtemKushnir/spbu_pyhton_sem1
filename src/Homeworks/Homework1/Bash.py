import os
import sys


def wc(argument, name_file):
    if argument == "-c":
        return os.path.getsize(name_file)
    elif argument == "-l":
        with open(name_file) as fl:
            return sum([line.count("\n") for line in fl])
    elif argument == "-w":
        with open(name_file) as fw:
            return sum([len(line.split())for line in fw])
    elif argument == "-m":
        with open(name_file) as fm:
            return sum([len(line) for line in fm])
    else:
        return None


def head(argument, name_file, value):
    if argument == "-n":
        with open(name_file) as fn:
            return "".join([line for i, line in enumerate(fn) if i < value])
    elif argument == "-c":
        with open(name_file) as fc:
            return fc.read(value)
    else:
        return None


def tail(argument, file_text, value):
    if argument == "-n":
        with open(file_text) as fn:
            return "".join(fn.readlines()[-value:])
    elif argument == "-c":
        with open(file_text) as fc:
            fc.seek(0, 2)
            fc_size = fc.tell()
            fc.seek(max(fc_size - value, 0), 0)
            return "".join([line for line in fc])
    else:
        return None


if __name__ == "__main__":
    arguments = sys.argv[1:]
    all_command = ["wc", "head", "tail"]
    all_option = ["-c", "-w", "-l", "-m", "-n"]
    file_name = arguments[-1]
    option, command, number = "", 0, 10
    for i in range(len(arguments)):
        if arguments[i] in all_command:
            command = arguments[i]
        elif arguments[i] in all_option:
            option = arguments[i]
            number = arguments[i + 1]
            break
    if command == "wc":
        if wc(option, file_name) is None:
            print("error")
        else:
            print(f"{command, option, file_name}:", wc(option, file_name))
    elif command == "head":
        if head(option, file_name, number) is None:
            print("error")
        else:
            print(f"{command, option, number, file_name}:", head(option, file_name, number))
    elif command == "tail":
        if tail(option, file_name, number) is None:
            print("error")
        else:
            print(f"{command, option, number, file_name}:", tail(option, file_name, number))
    else:
        print("error")
