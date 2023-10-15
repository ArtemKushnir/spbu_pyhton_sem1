def find_fractions(max_denominator):
    res = []
    for numerator in range(1, max_denominator):
        for denominator in range(numerator + 1, max_denominator + 1):
            if numerator == 1:
                res.append((numerator, denominator))
            elif find_divisors(
                max(numerator, denominator), min(numerator, denominator)
            ):
                res.append((numerator, denominator))
    res.sort(key=lambda x: x[0] / x[1])
    return res


def find_divisors(number1, number2):
    while number1 % number2 != 0:
        number1, number2 = number2, number1 % number2
    if number2 == 1:
        return True
    return False


def output_fractions(numerators_and_denominators):
    print("Все подходящие дроби:")
    fractions = map(
        lambda fraction: f"{fraction[0]}/{fraction[1]}", numerators_and_denominators
    )
    return ", ".join(fractions)


if __name__ == "__main__":
    print("Введите знаменатель:")
    n = input()
    if n.isdigit():
        n = int(n)
        if n <= 1:
            print("Ошибка, знаменатель должен быть больше 1")
        else:
            all_fractions = find_fractions(n)
            print(output_fractions(all_fractions))
    else:
        print("Ошибка! Введено не число")
