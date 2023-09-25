import csv


def read_file(file_read):
    all_words = {}
    with open(file_read) as file_txt:
        for line in file_txt:
            for word in line.lower().split():
                all_words[word] = all_words.get(word, 0) + 1
    return all_words


def record_file(file_record, all_words):
    with open(file_record, "w") as file_csv:
        writer = csv.writer(file_csv)
        writer.writerow(
            ("Слово", "Количество")
        )
        writer.writerows(zip(list(all_words.keys()), list(all_words.values())))


if __name__ == "__main__":
    print("Название файла для анализа:")
    file_name_read = input()
    print("Название файла для записи:")
    file_name_record = input()
    record_file(file_name_record, read_file(file_name_read))
