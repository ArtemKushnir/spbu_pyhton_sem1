def score(x):
    squared_x = x * x
    return (squared_x + 1) * (squared_x + x) + 1


if __name__ == "__main__":
    x = int(input("Чтобы посчитать значение выражения x^4+x^3+x^2+x+1, введите x: "))
    print(f"{x}^4+{x}^3+{x}^2+{x}+1 = {score(x)}")
