def read(file_read):
    with open(file_read) as f_read:
        m = int(f_read.readline())
        dna = f_read.readline()
        n = int(f_read.readline())
        res = []
        for i in range(n):
            name_command, first_argument, second_argument = f_read.readline().split()
            if name_command == "DELETE":
                dna = delete(dna, first_argument, second_argument)
                res.append(dna)
            elif name_command == "INSERT":
                dna = insert(dna, first_argument, second_argument)
                res.append(dna)
            elif name_command == "REPLACE":
                dna = replace(dna, first_argument, second_argument)
                res.append(dna)
    return res


def record(dna, file_record):
    with open(file_record, "w") as f_record:
        f_record.write("".join(dna))


def delete(dna, argument1, argument2):
    return (
        dna[: dna.find(argument1)]
        + dna[
            dna.find(argument2, dna.find(argument1) + len(argument1)) + len(argument2) :
        ]
    )


def insert(dna, argument1, argument2):
    return (
        dna[: dna.find(argument1) + len(argument1)]
        + argument2
        + dna[dna.find(argument1) + len(argument1) :]
    )


def replace(dna, argument1, argument2):
    return (
        dna[: dna.find(argument1)]
        + argument2
        + dna[dna.find(argument1) + len(argument1) :]
    )


if __name__ == "__main__":
    print("Название файла с исходными ДНК:")
    file_name_read = input()
    print("Название файла для записи")
    file_name_record = input()
    record(read(file_name_read), file_name_record)
