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


def get_fp_format(whole_part, fractional_part, sign, output_format):
    if output_format == "1":
        format_mantis, format_order, bit_for_order = 52, [-1023, 1024], 11
    elif output_format == "2":
        format_mantis, format_order, bit_for_order = 23, [-127, 128], 8
    else:
        format_mantis, format_order, bit_for_order = 10, [-15, 16], 6
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
    change_order = order + 2 ** (bit_for_order - 1) - 2
    if sign == "+":
        sign = "0"
    else:
        sign = "1"
    normal_after_point = normal_number[normal_number.find(".") + 2 :]
    binary_change_order = "{:0>{bit_order}}".format(
        bin(change_order)[2:], bit_order=bit_for_order
    )
    fp_format = (
        sign
        + " "
        + binary_change_order
        + " "
        + normal_after_point
        + "0" * (format_mantis - len(normal_after_point))
    )
    return fp_format, normal_number, order


def validate_real_number(number):
    try:
        float(number)
        return True
    except ValueError:
        return False


def main():
    real_number = input("enter a real number in decimal form: ")
    if validate_real_number(real_number):
        real_number = float(real_number)
        print("select the output format\n1.FP64\n2.FP32\n3.FP16")
        form = input("select the output format: ")
        if form not in "123":
            print("there is no such format")
        else:
            if real_number >= 0:
                sign = "+"
            else:
                sign = "-"
            try:
                fp_form, normal_form, order = get_fp_format(
                    abs(int(real_number)), abs(real_number) % 1, sign, form
                )
                print(f"number in normalized form: {normal_form} * 2^{order}")
                print("number in the selected format:", fp_form)
            except OverflowError:
                print("incorrect real number")
            except ValueError:
                print("wrong format")
    else:
        print("not a real number")


if __name__ == "__main__":
    main()
