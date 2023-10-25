def convert_to_normal_form_whole_part(whole_part, format_order):
    result = ""
    if whole_part == 0:
        return "0", 0
    while whole_part != 0:
        result += str(whole_part % 2)
        whole_part //= 2
    order = len(result)
    if not (format_order[0] <= order <= format_order[1]):
        raise ValueError("incorrect number")
    return "0." + result[::-1], order


def convert_to_normal_form_whole_0(fractional_part, format_mantis, format_oder):
    if fractional_part == 0:
        return "0.0", 0
    else:
        result, order, count_mantis = "0.", 0, 0
        flag = False
        while count_mantis < format_mantis:
            if int(fractional_part * 2) == 1:
                flag = True
            if flag:
                result += str(int(fractional_part * 2))
                count_mantis += 1
            else:
                order -= 1
            if fractional_part * 2 == 1:
                break
            if not (format_oder[0] <= order <= format_oder[1]):
                raise ValueError("incorrect number")
            fractional_part = (fractional_part * 2) % 1
    return result, order


def convert_to_normal_form_whole_no_0(
    whole_part, fractional_part, format_mantis, order
):
    if fractional_part == 0:
        return whole_part, order
    else:
        count_mantis = order
        result = whole_part
        while count_mantis < format_mantis:
            count_mantis += 1
            result += str(int(fractional_part * 2))
            if fractional_part * 2 == 1:
                break
            fractional_part = (fractional_part * 2) % 1
        return result, order


def output_fp_64(whole_part, fractional_part, sign):
    format_mantis, format_order = 52, [-1023, 1024]
    whole_normal_form, order = convert_to_normal_form_whole_part(
        whole_part, format_order
    )
    if whole_normal_form == "0":
        normal_number, order = convert_to_normal_form_whole_0(
            fractional_part, format_mantis, format_order
        )
    else:
        normal_number, order = convert_to_normal_form_whole_no_0(
            whole_normal_form, fractional_part, format_mantis, order
        )
    normal_number = sign + normal_number
    change_order = order + 2**10 - 2
    if sign == "+":
        sign = "0"
    else:
        sign = "1"
    normal_after_point = normal_number[normal_number.find(".") + 2 :]
    binary_change_order = (
        "0" * (11 - len(bin(change_order)[2:])) + bin(change_order)[2:]
    )
    fp_64 = (
        sign
        + " "
        + binary_change_order
        + " "
        + normal_after_point
        + "0" * (format_mantis - len(normal_after_point))
    )
    return fp_64, normal_number, order


def output_fp_32(whole_part, fractional_part, sign):
    format_mantis, format_order = 23, [-127, 128]
    whole_normal_form, order = convert_to_normal_form_whole_part(
        whole_part, format_order
    )
    if whole_normal_form == "0":
        normal_number, order = convert_to_normal_form_whole_0(
            fractional_part, format_mantis, format_order
        )
    else:
        normal_number, order = convert_to_normal_form_whole_no_0(
            whole_normal_form, fractional_part, format_mantis, order
        )
    normal_number = sign + normal_number
    change_order = order + 2**7 - 2
    if sign == "+":
        sign = "0"
    else:
        sign = "1"
    normal_after_point = normal_number[normal_number.find(".") + 2 :]
    binary_change_order = "0" * (8 - len(bin(change_order)[2:])) + bin(change_order)[2:]
    fp_32 = (
        sign
        + " "
        + binary_change_order
        + " "
        + normal_after_point
        + "0" * (format_mantis - len(normal_after_point))
    )
    return fp_32, normal_number, order


def output_fp_16(whole_part, fractional_part, sign):
    format_mantis, format_order = 10, [-15, 16]
    whole_normal_form, order = convert_to_normal_form_whole_part(
        whole_part, format_order
    )
    if whole_normal_form == "0":
        normal_number, order = convert_to_normal_form_whole_0(
            fractional_part, format_mantis, format_order
        )
    else:
        normal_number, order = convert_to_normal_form_whole_no_0(
            whole_normal_form, fractional_part, format_mantis, order
        )
    normal_number = sign + normal_number
    change_order = order + 2**5 - 2
    if sign == "+":
        sign = "0"
    else:
        sign = "1"
    normal_after_point = normal_number[normal_number.find(".") + 2 :]
    binary_change_order = "0" * (5 - len(bin(change_order)[2:])) + bin(change_order)[2:]
    fp_16 = (
        sign
        + " "
        + binary_change_order
        + " "
        + normal_after_point
        + "0" * (format_mantis - len(normal_after_point))
    )
    return fp_16, normal_number, order


def main_func(number, format_number):
    if number > 0:
        sign = "+"
    else:
        sign = "-"
    number = abs(number)
    whole_part, fractional_part = int(number), number % 1
    if format_number == 1:
        try:
            return output_fp_64(whole_part, fractional_part, sign)
        except ValueError as e:
            return str(e)
    elif format_number == 2:
        try:
            return output_fp_32(whole_part, fractional_part, sign)
        except ValueError as e:
            return str(e)
    else:
        try:
            return output_fp_16(whole_part, fractional_part, sign)
        except ValueError as e:
            return str(e)


if __name__ == "__main__":
    print("enter a real number in decimal form")
    try:
        real_number = float(input())
        print("select the output format")
        print("1.FP64\n2.FP32\n3.FP16")
        form = int(input("select the output format: "))
        fp_form, normal_form, order = main_func(real_number, form)
        print(f"number in normalized form: {normal_form} * 2^{order}")
        print("number in the selected format:", fp_form)
    except ValueError:
        print("not a number")
