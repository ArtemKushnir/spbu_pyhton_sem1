def transformation_to_binary(number):
    if number == 0:
        return [0, 0]
    elif number > 0:
        sign = [0]
    else:
        number = abs(number)
        sign = [1]
    bit = []
    while number:
        bit.append(number % 2)
        number //= 2
    bit.append(0)
    return sign + bit[::-1]


def transformation_to_additional(number):
    if number[0] == 0:
        return number
    for i in range(1, len(number)):
        if number[i] == 0:
            number[i] = 1
        else:
            number[i] = 0
    return calculate_sum(number, [0] * (len(number) - 1) + [1])


def add_digits_to_second_number(number1, number2, negative_number2):
    for i in range(len(number1) - len(number2)):
        number2.insert(1, 0)
        negative_number2.insert(1, 0)
    return number2, negative_number2


def add_digits_to_first_number(number1, number2):
    for i in range(len(number2) - len(number1)):
        number1.insert(1, 0)
    return number1


def calculate_final_number(number1, number2):
    direct_code1 = transformation_to_binary(number1)
    direct_code2 = transformation_to_binary(number2)
    direct_negative_code2 = transformation_to_binary(-number2)
    if len(direct_code1) > len(direct_code2):
        direct_code2, direct_negative_code2 = add_digits_to_second_number(
            direct_code1, direct_code2, direct_negative_code2
        )
    elif len(direct_code2) > len(direct_code1):
        direct_code1 = add_digits_to_first_number(direct_code1, direct_code2)
    additional_code1 = transformation_to_additional(direct_code1)
    additional_code2 = transformation_to_additional(direct_code2)
    additional_negative_code2 = transformation_to_additional(direct_negative_code2)
    return additional_code1, additional_code2, additional_negative_code2


def calculate_sum(number1, number2):
    result = []
    count = 0
    for i in range(len(number1) - 1, -1, -1):
        adding_digit = number1[i] + number2[i] + count
        result.append(adding_digit % 2)
        if adding_digit > 1:
            count = 1
        else:
            count = 0
    return result[::-1]


def output_numbers_and_calculations(
    binary_number1, binary_number2, binary_reverse, number1, number2
):
    binary_number1_string = "".join(map(str, binary_number1))
    binary_number2_string = "".join(map(str, binary_number2))
    print("The first number in binary form:", binary_number1_string)
    print("The second number in binary form:", binary_number2_string)
    print("The sum in binary form:")
    binary_sum = "".join(map(str, calculate_sum(binary_number1, binary_number2)))
    print(f"{binary_number1_string} + {binary_number2_string} = {binary_sum}")
    print("The sum in decimal form:")
    print(f"{number1} + {number2} = {number1 + number2}")
    print("The difference in binary form:")
    difference = "".join(map(str, calculate_sum(binary_number1, binary_reverse)))
    print(f"{binary_number1_string} - {binary_number2_string} = {difference}")
    print("The difference in decimal form:")
    print(f"{number1} - {number2} = {number1 - number2}")


def main():
    print("Enter first number:")
    first_number = input()
    if not first_number.lstrip("-").isdigit():
        print("error, not a number entered")
        return
    print("Enter second number:")
    second_number = input()
    if not second_number.lstrip("-").isdigit():
        print("error, not a number entered")
        return
    first_code, second_code, second_reverse_code = calculate_final_number(
        int(first_number), int(second_number)
    )
    output_numbers_and_calculations(
        first_code,
        second_code,
        second_reverse_code,
        int(first_number),
        int(second_number),
    )


if __name__ == "__main__":
    main()
