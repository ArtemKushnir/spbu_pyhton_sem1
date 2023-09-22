import random


def bulls_and_cows(n1, n2, length):
    cows = 0
    bulls = 0
    for i in range(length):
        if n1[i] == n2[i]:
            bulls += 1
        elif n1[i] in n2:
            cows += 1
    if bulls == length:
        return None
    return [bulls, cows]


def game(n, my_number, k):
    while True:
        if bulls_and_cows(n, my_number, k) is None:
            print("Вы выиграли")
            break
        else:
            print(f"Быки: {bulls_and_cows(n, my_number, k)[0]}")
            print(f"Коровы: {bulls_and_cows(n, my_number, k)[1]}")
            print("Введите новое число:")
            n = input()


if __name__ == "__main__":
    print("Это игра 'Быки и коровы'")
    print("Введите количество цифр в числе для игры:")
    k = int(input())
    number = ''.join(str(element) for element in ([1] + (random.sample(range(0, 9), k - 1))))
    print("Введите число:")
    n = input()
    game(n, number, k)
