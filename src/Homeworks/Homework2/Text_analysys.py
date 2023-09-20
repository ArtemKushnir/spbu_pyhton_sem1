import csv


def read_file(file_read, file_record):
    all_words = {}
    with open(file_read) as file_txt:
        for line in file_txt:
            for word in line.lower().split():
                if word in all_words:
                    all_words[word] += 1
                else:
                    all_words[word] = 1

    record_file(file_record, all_words)


def record_file(file_record, all_words):
    with open(file_record, "w") as file_csv:
        writer = csv.writer(file_csv)
        writer.writerow(
            ("Слово", "Количество")
        )
        for i in all_words:
            writer.writerow(
                [i, all_words[i]]
            )


if __name__ == "__main__":
    print("Название файла для анализа:")
    file_name_read = input()
    print("Название файла для записи:")
    file_name_record = input()
    read_file(file_name_read, file_name_record)
