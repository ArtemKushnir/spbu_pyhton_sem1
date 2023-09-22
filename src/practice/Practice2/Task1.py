def fractions(n):
    res = []
    for n1 in range(2, n + 1):
        for n2 in range(1, n1):
            if common_divisors(n1, n2):
                res.append(f"{n2}/{n1}")
    return res


def common_divisors(n1, n2):
    for i in range(2, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            return False
    return True


if __name__ == "__main__":
    print("Введите число n")
    n = int(input())
    if n <= 1:
        print("Ошибка")
    else:
        print(f"Все подходящие дроби:", ", ".join(fractions(n)))
