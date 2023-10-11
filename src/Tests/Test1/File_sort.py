import sys
import os


def read_and_process(first_number, second_number, file_input):
    with open(file_input) as f_input:
        all_numbers = [int(i) for i in f_input.readline().split()]
        all_groups = {"first": [], "second": [], "third": []}
        for i in all_numbers:
            if i < first_number:
                all_groups["first"] += str(i)
            elif first_number <= i <= second_number:
                all_groups["second"] += str(i)
            else:
                all_groups["third"] += str(i)
    return all_groups


def writing_file(file_output, result):
    with open(file_output, "w") as f_output:
        f_output.write(" ".join(result["first"]) + "\n")
        f_output.write(" ".join(result["second"]) + "\n")
        f_output.write(" ".join(result["third"]))


if __name__ == "__main__":
    a, b, f, g = sys.argv[1:]
    if not os.path.isfile(f):
        print(f"Файл {f} не существует")
    elif os.path.isfile(g):
        print(f"Файл {g} уже существует")
    else:
        writing_file(g, read_and_process(a, b, f))
