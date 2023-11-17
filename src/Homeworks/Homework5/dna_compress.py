from itertools import groupby


def encode_string(string):
    return "".join([f"{i}{len(list(g))}" for i, g in groupby(string)])


def decode_string(string):
    result = ""
    letter = string[0]
    index_letter = 0
    for i in range(2, len(string)):
        if string[i].isalpha():
            result += letter * int(string[index_letter + 1: i])
            letter = string[i]
            index_letter = i
    result += letter * int(string[index_letter + 1:])
    return result


def validate_input(string):
    if string.isalpha():
        return "1"
    pod_string = ""
    count_alpha = 0



def main():
    dna = input("Enter DNA: ")
    print("1.Encode DNA\n2.Decode DNA")
    number_operation = input("Enter number: ")
    acceptable_numbers = validate_input(dna[::-1])
    if number_operation not in "12":
        print("incorrect transaction number")
    elif number_operation == "1" and number_operation in acceptable_numbers:
        print(encode_string(dna))
    elif number_operation == "2" and number_operation in acceptable_numbers:
        print(decode_string(dna))
    else:
        print("incorrect dna for this operation")


if __name__ == "__main__":
    main()
