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
    return bit + sign


def transformation_to_additional(number_array):
    if number_array[-1] == 0:
        return number_array
    for i in range(len(number_array) - 1):
        if number_array[i] == 0:
            number_array[i] = 1
        else:
            number_array[i] = 0
    return calculate_sum(number_array, [1] + [0] * (len(number_array) - 1))


def add_digits(number_array, difference_length):
    number_array = number_array[:-1]
    sign = number_array[-1]
    number_array.extend([sign] * difference_length)
    number_array.append(sign)
    return number_array


def calculate_sum(number1_array, number2_array):
    result = []
    count = 0
    for i in range(len(number1_array)):
        adding_digit = number1_array[i] + number2_array[i] + count
        result.append(adding_digit % 2)
        count = adding_digit // 2
    return result


def transformation_to_decimal(number_array):
    sign = 1
    if number_array[-1] == 1:
        sign = -1
        number_array = calculate_sum(number_array, [1] * len(number_array))
        for i in range(len(number_array)):
            if number_array[i] == 0:
                number_array[i] = 1
            else:
                number_array[i] = 0
    result = 0
    for i in range(len(number_array)):
        result += 2**i * number_array[i] * sign
    return result


def calculate_final_numbers(number1, number2):
    number1_array = transformation_to_additional(transformation_to_binary(number1))
    number2_array = transformation_to_additional(transformation_to_binary(number2))
    negative_number2_array = transformation_to_additional(
        transformation_to_binary(-number2)
    )
    digit_difference = abs(len(number1_array) - len(number2_array))
    if len(number1_array) > len(number2_array):
        number2_array = add_digits(number2_array, digit_difference)
        negative_number2_array = add_digits(negative_number2_array, digit_difference)
    elif len(number2_array) > len(number1_array):
        number1_array = add_digits(number1_array, digit_difference)
    return number1_array, number2_array, negative_number2_array


if __name__ == "__main__":
    print("enter first number:")
    first_number = int(input())
    print("enter second number:")
    second_number = int(input())
    first_number, second_number, negative_second_number = calculate_final_numbers(
        first_number, second_number
    )
    print("first number in binary form:", "".join(map(str, first_number[::-1])))
    print("second number in binary form:", "".join(map(str, second_number[::-1])))
    binary_sum_reverse = calculate_sum(first_number, second_number)
    print("sum in binary form:", "".join(map(str, binary_sum_reverse[::-1])))
    print("sum in decimal form:", transformation_to_decimal(binary_sum_reverse)),
    binary_difference_reverse = calculate_sum(first_number, negative_second_number)
    print(
        "difference in binary form:", "".join(map(str, binary_difference_reverse[::-1]))
    )
    print(
        "difference in decimal form:",
        transformation_to_decimal(binary_difference_reverse),
    )
