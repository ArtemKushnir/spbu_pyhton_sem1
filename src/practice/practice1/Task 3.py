def prime(number):
    d = 2
    while d * d <= number:
        if number % d == 0:
            return False
        d += 1
    return True


if __name__ == "__main__":
    print("Введите число")
    n = int(input())
    numbers = []
    for i in range(2, n + 1):
        if prime(i):
            numbers.append(str(i))
    print("Простые числа:", ", ".join(numbers))