import re


def read(file_read, file_record):
    with open(file_read) as f_read:
        m = int(f_read.readline())
        dna = f_read.readline()
        if re.compile("[ACGT]").search(dna) is None:
            return None
        else:
            n = int(f_read.readline())
            for i in range(n):
                line_command = f_read.readline().split()
                if line_command[0] == "DELETE":
                    dna = delete(dna, line_command[1:])
                    record(dna, file_record)
                elif line_command[0] == "INSERT":
                    dna = insert(dna, line_command[1:])
                    record(dna, file_record)
                elif line_command[0] == "REPLACE":
                    dna = replace(dna, line_command[1:])
                    record(dna, file_record)
    return True

def record(dna, file_record):
    with open(file_record, "a") as f_record:
        f_record.write(dna)


def delete(dna, commands):
    pattern = re.compile(f'{commands[0]}\w*{commands[1]}').search(dna)
    if pattern is None:
        return dna
    else:
        return dna[:pattern.start()] + dna[pattern.end():]


def insert(dna, commands):
    pattern = re.compile(f'{commands[0]}').search(dna)
    if pattern is None:
        return dna
    else:
        return dna[:pattern.end()] + commands[1] + dna[pattern.end():]


def replace(dna, commands):
    pattern = re.compile(f'{commands[0]}').search(dna)
    if pattern is None:
        return dna
    else:
        return dna[:pattern.start()] + commands[1] + dna[pattern.end():]


if __name__ == "__main__":
    print("Название файла с исходными ДНК:")
    file_name_read = input()
    print("Название файла для записи")
    file_name_record = input()
    if read(file_name_read, file_name_record) is None:
        print("error")
    else:
        read(file_name_read, file_name_record)