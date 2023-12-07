from itertools import groupby


def encode_string(string: str) -> str:
    return "".join([f"{i}{len(list(g))}" for i, g in groupby(string)])


def decode_string(string: str) -> str:
    letters = "".join(
        map(lambda letter: letter if letter.isalpha() else " ", string)
    ).split()
    numbers = "".join(
        map(lambda number: number if number.isdigit() else " ", string)
    ).split()
    return "".join(
        map(lambda index: letters[index] * int(numbers[index]), range(len(letters)))
    )


def validate_input_for_encode(string: str) -> bool:
    if string.isalpha():
        return True
    return False


def validate_input_for_decode(string: str) -> bool:
    if not (string[0].isalpha()):
        return False
    previous_letter = 0
    number = ""
    for i in range(1, len(string)):
        if not (string[i].isdigit() or string[i].isalpha()):
            return False
        if string[i].isalpha():
            number = string[previous_letter + 1 : i]
            previous_letter = i
            if len(number) == 0 or number[0] == "0":
                return False
            number = ""
        else:
            number += string[i]
    if len(number) == 0 or number[0] == "0":
        return False
    return True


def main() -> None:
    dna = input("Enter DNA: ")
    print("1.Encode DNA\n2.Decode DNA")
    number_operation = input("Enter number: ")
    if number_operation == "1":
        if validate_input_for_encode(dna):
            print(encode_string(dna))
        else:
            print("incorrect dna for encode")
    elif number_operation == "2":
        if validate_input_for_decode(dna):
            print(decode_string(dna))
        else:
            print("incorrect dna for decode")
    else:
        print("incorrect transaction number")


if __name__ == "__main__":
    main()
