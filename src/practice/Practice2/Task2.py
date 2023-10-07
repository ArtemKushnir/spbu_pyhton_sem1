import random


def counting_bulls_and_cows(user_number, my_number):
    cows = 0
    bulls = 0
    length = 4
    for i in range(length):
        if user_number[i] == my_number[i]:
            bulls += 1
        elif user_number[i] in my_number:
            cows += 1
    return [bulls, cows]


def determine_result(user_number, my_number):
    while True:
        bulls, cows = counting_bulls_and_cows(user_number, my_number)
        print(bulls, cows)
        if bulls == 4:
            print("Вы выиграли")
            break
        else:
            print(f"Быки: {bulls}")
            print(f"Коровы: {cows}")
            print("Введите новое число:")
            user_number = input()
            if not user_number.isdigit():
                print("Ошибка, введено не число")
                break
            elif user_number[0] == "0":
                print("Ошибка, первая цифра не может быть нулем")
                break


if __name__ == "__main__":
    print("Это игра 'Быки и коровы'")
    all_digits = [str(i) for i in range(10)]
    random.shuffle(all_digits)
    if all_digits[0] == "0":
        random_number = "".join(all_digits[1:5])
    else:
        random_number = "".join(all_digits[:4])
    print("Введите четырехзначное число:")
    n = input()
    if not n.isdigit():
        print("Ошибка, введено не число")
    elif n[0] == "0":
        print("Ошибка, первая цифра не может быть нулем")
    else:
        determine_result(n, random_number)
