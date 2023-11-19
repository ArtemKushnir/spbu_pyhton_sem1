from itertools import groupby


def encode_string(string: str) -> str:
    return "".join([f"{i}{len(list(g))}" for i, g in groupby(string)])


def decode_string(string: str) -> str:
    k = 2
    result = ""
    while string != "$":
        if string[k].isalpha():
            result += string[0] * int(string[1:k])
            string = string[k:]
            k = 0
        elif string[k] == "$":
            result += string[0] * int(string[1:-1])
            break
        k += 1
    return result


def validate_input(string: str) -> str:
    if string[:-1].isalpha():
        return "1"
    if string[0].isalpha():
        for i in range(len(string) - 1):
            if string[i].isalpha() and not (string[i + 1].isdigit() and string[i + 1] != "0"):
                return ""
            if not (string[i].isalpha() or string[i].isdigit()):
                return ""
        return "2"
    return ""


def main() -> None:
    dna = input("Enter DNA: ")
    acceptable_number = validate_input(dna)
    print(acceptable_number)
    print("1.Encode DNA\n2.Decode DNA")
    number_operation = input("Enter number: ")
    if number_operation == acceptable_number == "1":
        print(encode_string(dna))
    elif number_operation == acceptable_number == "2":
        print(decode_string(dna + "$"))
    elif acceptable_number != number_operation:
        print("incorrect dna")
    else:
        print("incorrect transaction number")


if __name__ == "__main__":
    main()
