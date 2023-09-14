def permutation(numbers, m, n):
    numbers[:m], numbers[m:m+n] = numbers[m-1::-1], numbers[m + n - 1:m - 1:-1]
    return numbers[::-1]


if __name__ == "__main__":
    print('Введите m')
    m = int(input())
    print('Введите n')
    n = int(input())
    print('Введите числа массива через пробел')
    numbers = input()
    numbers = numbers.split()
    print("Вот новый массив:", ", ".join(permutation(numbers, m, n)))