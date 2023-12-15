from src.practice.practice_10 import parser


def main() -> None:
    input_string = input("Enter a string for parsing: ")
    try:
        parse_tree = parser.parse(input_string.split())
        print(input_string, "=:")
        parser.pretty_print(parse_tree)
    except ValueError as e:
        print(str(e))


if __name__ == "__main__":
    main()
