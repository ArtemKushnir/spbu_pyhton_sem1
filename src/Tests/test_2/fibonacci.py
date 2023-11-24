def get_fibonacci_number(n: int) -> int:
    curr_number = 0
    next_number = 1
    for i in range(n):
        curr_number, next_number = next_number, curr_number + next_number
    return curr_number


def validate_input(n: str) -> int:
    if not n.lstrip("-").isdigit():
        raise ValueError("it's not an integer")
    if not (0 <= int(n) <= 90):
        raise ValueError("wrong number")
    return int(n)


def main() -> None:
    n = input("enter the number of the fibonacci number from 0 to 90: ")
    try:
        n = validate_input(n)
        print(f"fibonacci number number {n} = {get_fibonacci_number(n)}")
    except ValueError as e:
        print(str(e))


if __name__ == "__main__":
    main()
