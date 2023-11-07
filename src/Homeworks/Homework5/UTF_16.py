def get_size(string):
    for symbol in string:
        if ord(symbol) > 65535:
            return 4
    return 2


def encode(code_string, size_byte):
    result = []
    for symbol in code_string:
        hex_code = "U+" + "{:0>4}".format(hex(ord(symbol))[2:].upper())
        if size_byte == 2:
            binary_code = "{:0>16}".format(bin(ord(symbol))[2:])
        else:
            binary_code = encode_binary_4_byte(symbol)
        binary_code = " ".join(
            binary_code[i : i + 8] for i in range(0, len(binary_code), 8)
        )
        result.append((symbol, hex_code, binary_code))
    return result


def encode_binary_4_byte(symbol):
    if ord(symbol) > 65535:
        binary_code_20_points = "{:0>20}".format(bin(ord(symbol) - 65536)[2:])
        first_part = binary_code_20_points[:10]
        second_part = binary_code_20_points[10:]
        first_2_byte = bin(int(first_part, 2) + 55296)[2:]
        second_2_byte = bin(int(second_part, 2) + 56320)[2:]
        return first_2_byte + second_2_byte
    else:
        return "{:0>32}".format(bin(ord(symbol))[2:])


if __name__ == "__main__":
    string = input("Enter a string: ")
    for i in encode(string, get_size(string)):
        print(f"{i[0]}\t{i[1]}\t{i[2]}")
