def transformation_to_binary(number):
    if number == 0:
        return [0, 0]
    elif number > 0:
        bit = []
        sign = [0, 0]
    else:
        bit = []
        number = abs(number)
        sign = [1, 0]
    while number:
        bit.append(number % 2)
        number //= 2
    return sign + bit[::-1]


def transformation_to_reverse(number):
    if number[0] == 0:
        return number
    else:
        for i in range(1, len(number)):
            if number[i] == 0:
                number[i] = 1
            else:
                number[i] = 0
        return number


def transformation_to_additional(number):
    if number[0] == 0:
        return number
    else:
        for i in range(len(number) - 1, 0, -1):
            if number[i] == 0:
                return number[:i] + [1] + [0] * (len(number) - i - 1)


def change(number1, number2, negative_number2):
    if len(number1) > len(number2):
        number2 = [number2[0]] + [0] * (len(number1) - len(number2)) + number2[1:]
        negative_number2 = (
            [negative_number2[0]]
            + [0] * (len(number1) - len(negative_number2))
            + negative_number2[1:]
        )
        return number1, number2, negative_number2
    elif len(number2) > len(number1):
        number1 = [number1[0]] + [0] * (len(number2) - len(number1)) + number1[1:]
        return number1, number2, negative_number2
    else:
        return number1, number2, negative_number2


def calculate_final_number(number1, number2):
    direct_code1 = transformation_to_binary(number1)
    direct_code2 = transformation_to_binary(number2)
    direct_negative_code2 = transformation_to_binary(-number2)
    direct_code1, direct_code2, direct_negative_code2 = change(
        direct_code1, direct_code2, direct_negative_code2
    )
    reverse_code1 = transformation_to_reverse(direct_code1)
    reverse_code2 = transformation_to_reverse(direct_code2)
    reverse_negative_code2 = transformation_to_reverse(direct_negative_code2)
    additional_code1 = transformation_to_additional(reverse_code1)
    additional_code2 = transformation_to_additional(reverse_code2)
    additional_negative_code2 = transformation_to_additional(reverse_negative_code2)
    return additional_code1, additional_code2, additional_negative_code2


def calculate_sum(number1, number2):
    result = []
    count = 0
    for i in range(len(number1) - 1, -1, -1):
        if number1[i] + number2[i] + count == 0:
            result.append(0)
            count = 0
        elif number1[i] + number2[i] + count == 1:
            result.append(1)
            count = 0
        elif number1[i] + number2[i] + count == 2:
            result.append(0)
            count = 1
        else:
            result.append(1)
            count = 1
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


if __name__ == "__main__":
    print("Enter first number:")
    first_number = int(input())
    print("Enter second number:")
    second_number = int(input())
    first_code, second_code, second_reverse_code = calculate_final_number(
        first_number, second_number
    )
    output_numbers_and_calculations(
        first_code, second_code, second_reverse_code, first_number, second_number
    )
