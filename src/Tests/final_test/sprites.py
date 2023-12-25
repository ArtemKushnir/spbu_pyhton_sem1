import random


BLACK_SQUARE = "■"
WHITE_SQUARE = "□"


def create_horizontal_and_vertical_symmetry(matrix, size):
    return create_horizontal_symmetry(create_vertical_symmetry(matrix, size), size)


def create_horizontal_symmetry(matrix, size):
    for x in range((size // 2) + 1):
        matrix[size - 1 - x] = matrix[x]
    return matrix


def create_vertical_symmetry(matrix, size):
    horizontal_matrix = create_horizontal_symmetry(matrix, size)
    transposition_matrix = [
        [horizontal_matrix[i][j] for i in range(size)] for j in range(size)
    ]
    return transposition_matrix


def create_sprite_matrix(size):
    random_symmetry = random.randint(1, 3)
    matrix = [[random.randint(0, 1) for j in range(size)] for i in range(size)]
    if random_symmetry == 1:
        return create_vertical_symmetry(matrix, size)
    if random_symmetry == 2:
        return create_horizontal_symmetry(matrix, size)
    else:
        return create_horizontal_and_vertical_symmetry(matrix, size)


def pretty_print_sprite(matrix):
    for i in matrix:
        string = ""
        for j in i:
            if j == 0:
                string += WHITE_SQUARE
            else:
                string += BLACK_SQUARE

        print(string)


def main():
    sprite_size = input("Enter a number - sprite size in pixels: ")
    if sprite_size.isdigit() and int(sprite_size) > 1:
        sprite_size = int(sprite_size)
        print("To output the next sprite, press enter, and to finish, type end: ")
        user_input = input()
        while user_input != "end":
            if user_input != "":
                print("incorrect input")
            else:
                pretty_print_sprite(create_sprite_matrix(sprite_size))
            user_input = input()
    else:
        print("error sprite size")


if __name__ == "__main__":
    main()
