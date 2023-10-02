def division(a, b):
    k = 0
    while a > b:
        k += 1
        a -= b
    return k


if __name__ == "__main__":
    print("Неполное частное от деления a на b")
    print("Введите число a")
    a = int(input())
    print("Введите число b")
    b = int(input())
    print(
        f"Неполное частное от деления a на b: {division(a, b)}, остаток: {a - b*division(a, b)}"
    )
