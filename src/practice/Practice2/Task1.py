def fractions(n):
    res = {}
    for n1 in range(1, n):
        for n2 in range(n1 + 1, n + 1):
            if n1 / n2 not in res.values():
                res[f"{n1}/{n2}"] = n1 / n2
    return dict(sorted(res.items(), key=lambda item: item[1]))


if __name__ == "__main__":
    print("Введите число n")
    n = int(input())
    if n <= 1:
        print("Ошибка, знаменатель должен быть больше 1")
    else:
        print("Все подходящие дроби:")
        print(", ".join(fractions(n).keys()))
