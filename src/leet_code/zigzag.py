def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s
    rows = [""] * numRows
    number_string = 0
    next_movie = -1
    for char in s:
        rows[number_string] += char
        if number_string == 0:
            next_movie = 1
        elif number_string == numRows - 1:
            next_movie = -1
        number_string += next_movie
    return "".join(rows)


def main():
    s = input("Enter string: ")
    rows = input("Enter rows for record string: ")
    if rows.isdigit():
        print("string after transformations:", convert(s, int(rows)))
    else:
        print("rows must be integer")


if __name__ == "__main__":
    main()
