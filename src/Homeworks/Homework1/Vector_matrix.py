from math import *


def get_vector_scalar_product(
    first_vector, second_vector
):  # функция скалярного произведения векторов
    return sum([i[0] * i[1] for i in list(zip(first_vector, second_vector))])


def get_vector_length(coordinates):  # функция длины вектора
    return (sum([x**2 for x in coordinates])) ** 0.5


def get_vector_angle(first_vector, second_vector):  # фунуция угла между векторами
    return degrees(
        acos(
            (get_vector_scalar_product(first_vector, second_vector))
            / (get_vector_length(first_vector) * get_vector_length(second_vector))
        )
    )


def get_matrix_transposition(
    matrix, lines, columns
):  # функция транспонирования матрицы
    return [[matrix[j][i] for j in range(lines)] for i in range(columns)]


def get_matrix_addition(
    first_matrix, second_matrix, lines, columns
):  # функция сложения матриц
    return [
        [first_matrix[j][i] + second_matrix[j][i] for i in range(columns)]
        for j in range(lines)
    ]


def get_matrix_multiplication(
    first_matrix, second_matrix, lines1, columns1, lines2, columns2
):  # функция произведения матриц
    return [
        [
            get_vector_scalar_product(i, j)
            for j in get_matrix_transposition(second_matrix, lines2, columns2)
        ]
        for i in first_matrix
    ]


def select_action_vector():
    print(
        "Доступны 3 вида операций над векторами:\n1.Скалярное произведение\n2.Вычисление длины\n"
        "3.Нахождение угла."
    )
    operation_vector = input()

    if operation_vector == "1":
        select_scalar_product_vector()

    elif operation_vector == "2":
        select_length_vector()

    elif operation_vector == "3":
        select_angle_vector()

    else:
        print("Некоректный ввод")


def select_scalar_product_vector():
    print(
        "Для корректной работы важно, чтобы оба вектора содержали одинаковое количество кординат!"
    )
    print("Введите через пробел кординаты первого вектора:")
    first_vector = [int(i) for i in input().split()]
    print("Введите через пробел кординаты второго вектора:")
    second_vector = [int(i) for i in input().split()]
    if len(first_vector) != len(second_vector):
        print("Ошибка! Вы ввели векторы с разным количеством кординат.")
    else:
        print(
            "Скалярное произведение равно",
            get_vector_scalar_product(first_vector, second_vector),
        )


def select_length_vector():
    print("Введите через пробел кординаты вектора:")
    vector = [int(i) for i in input().split()]
    print("Длина вектора равна", get_vector_length(vector))


def select_angle_vector():
    print(
        "Для корректной работы важно, чтобы оба вектора содержали одинаковое количество кординат!"
    )
    print("Введите через пробел кординаты первого вектора:")
    first_vector = [int(i) for i in input().split()]
    print("Введите через пробел кординаты второго вектора:")
    second_vector = [int(i) for i in input().split()]
    if len(first_vector) != len(second_vector):
        print("Ошибка! Вы ввели векторы с разным количеством кординат.")
    else:
        print(
            f"Угол между векторами равен {round(get_vector_angle(first_vector, second_vector), 2)}°"
        )


def select_action_matrix():
    print(
        "Доступны 3 вида операций над матрицами:\n1.Транспонирование\n2.Сложение\n3.Произведение"
    )
    operation_matrix = input()
    print(
        "Для корректной работы важно, чтобы все строчки матрицы содержали одиннаковое количество значений!"
    )

    if operation_matrix == "1":
        select_transposition_matrix()

    elif operation_matrix == "2":
        select_addition_matrix()

    elif operation_matrix == "3":
        select_product_matrix()

    else:
        print("Некоректный ввод")


def select_transposition_matrix():
    print("Введите количество строк в вашей матрице:")
    lines_matrix = int(input())
    print("Введите количество столбцов в вашей матрице:")
    columns_matrix = int(input())
    print("По одной строке, вводите значения матрицы через пробел:")
    matrix = []
    for i in range(lines_matrix):
        matrix.append([int(i) for i in input().split()])
        if len(matrix[i]) != columns_matrix:
            print("Ошибка! В строчках матрицы разное количество элементов!")
            break
    else:
        print("Транспонированная матрица:")
        for j in get_matrix_transposition(matrix, lines_matrix, columns_matrix):
            print(*j)


def select_addition_matrix():
    print(
        "Чтобы произвести сложение матриц, нужно, чтобы они были одинаковой размерности."
    )
    print("Введите количество строк в ваших матрицах:")
    lines_matrix = int(input())
    print("Введите количество столбцов в ваших матрицах")
    columns_matrix = int(input())
    print("По одной строке, вводите значения первой матрицы через пробел:")
    matrix_first = []
    matrix_second = []
    for i in range(lines_matrix):
        matrix_first.append([int(i) for i in input().split()])
        if len(matrix_first[i]) != columns_matrix:
            print("Ошибка! В строчках первой матрицы разное количество элементов!")
            break
    else:
        print("По одной строке, вводите значения второй матрицы через пробел:")
        for j in range(lines_matrix):
            matrix_second.append([int(i) for i in input().split()])
            if len(matrix_second[j]) != columns_matrix:
                print("Ошибка! В строчках второй матрицы разное количество элементов!")
                break
        else:
            print("Результат сложения матриц:")
            for line in get_matrix_addition(
                matrix_first, matrix_second, lines_matrix, columns_matrix
            ):
                print(*line)


def select_product_matrix():
    print(
        "Чтобы произвести произведение матриц, нужно, чтобы количество столбцов первой матрицы равнялось "
        "количество строк второй матрицы, либо наоборот."
    )
    print("Введите количество строк первой матрицы:")
    first_lines_matrix = int(input())
    print("Введите количество столбцов первой матрицы")
    first_columns_matrix = int(input())
    print("По одной строке, вводите значения первой матрицы через пробел:")
    matrix_first = []
    matrix_second = []
    for i in range(first_lines_matrix):
        matrix_first.append([int(i) for i in input().split()])
        if len(matrix_first[i]) != first_columns_matrix:
            print("Ошибка! В строчках первой матрицы разное количество элементов!")
            break
    else:
        print("Введите количество строк второй матрицы:")
        second_lines_matrix = int(input())
        print("Введите количество столбцов второй матрицы:")
        second_columns_matrix = int(input())
        flag = True
        if not (
            first_columns_matrix == second_lines_matrix
            or first_lines_matrix == second_columns_matrix
        ):
            print("Такие матрицы невозможно перемножить!")
            flag = False
        if flag:
            print("По одной строке, вводите значения второй матрицы через пробел:")
            for j in range(second_lines_matrix):
                matrix_second.append([int(i) for i in input().split()])
                if len(matrix_second[j]) != second_columns_matrix:
                    print(
                        "Ошибка! В строчках второй матрицы разное количество элементов!"
                    )
                    break
            else:
                if first_columns_matrix == second_lines_matrix:
                    print("Результат умножения матриц:")
                    for line in get_matrix_multiplication(
                        matrix_first,
                        matrix_second,
                        first_lines_matrix,
                        first_columns_matrix,
                        second_lines_matrix,
                        second_columns_matrix,
                    ):
                        print(*line)
                elif first_lines_matrix == second_columns_matrix:
                    print("Результат умножения матриц:")
                    for line in get_matrix_multiplication(
                        matrix_second,
                        matrix_first,
                        second_lines_matrix,
                        second_columns_matrix,
                        first_lines_matrix,
                        first_columns_matrix,
                    ):
                        print(*line)


if __name__ == "__main__":
    print("Выберите с чем хотите работать:\n1.Векторы\n2.Матрицы")
    model = input()

    if model == "1":
        select_action_vector()

    elif model == "2":
        select_action_matrix()

    else:
        print("Некоректный ввод")
