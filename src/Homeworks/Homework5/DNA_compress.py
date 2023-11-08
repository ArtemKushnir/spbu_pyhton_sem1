from itertools import groupby


def encode_string(string):
    return "".join([f"{i}{len(list(g))}" for i, g in groupby(string)])


def decode_string(string):
    return "".join(string[i] * int(string[i + 1]) for i in range(0, len(string), 2))


def validate_input_encode(string):
    if not (string.isalpha()):
        raise ValueError("incorrect DNA, encoding operation cannot be performed")


def validate_input_decode(string):
    last_letter = ""
    for i in range(0, len(string), 2):
        if not (
            string[i].isalpha() and string[i + 1].isdigit() and string[i] != last_letter
        ):
            raise ValueError("incorrect DNA, decoding operation cannot be performed")
        last_letter = string[i]


if __name__ == "__main__":
    print("1.Encode DNA\n2.Decode DNA")
    number_operation = input("Enter number: ")
    if number_operation == "1":
        dna = input("Enter DNA: ")
        try:
            validate_input_encode(dna)
            print(encode_string(dna))
        except ValueError as e:
            print(str(e))
    elif number_operation == "2":
        dna = input("Enter DNA: ")
        try:
            validate_input_decode(dna)
            print(decode_string(dna))
        except ValueError as e:
            print(str(e))
    else:
        print("incorrect transaction number")
