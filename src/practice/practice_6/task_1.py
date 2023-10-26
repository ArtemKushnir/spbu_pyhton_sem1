def solve_equations(a, b, c):
    if a != 0:
        return tuple(sorted(solve_quadratic_equation(a, b, c)))
    elif b != 0:
        return solve_linear_equation(b, c)
    return solve_constant_equation(c)


def solve_quadratic_equation(a, b, c):
    d = b**2 - 4 * a * c
    if d == 0:
        if b == 0:
            return (b / (2 * a),)
        return (-b / (2 * a),)
    elif d > 0:
        return (-b + d**0.5) / (2 * a), (-b - d**0.5) / (2 * a)
    raise ArithmeticError("To find real roots discriminant must be non-negative")


def solve_linear_equation(b, c):
    return (-c / b,)


def solve_constant_equation(c):
    if c != 0:
        raise ArithmeticError("no solutions")
    raise ArithmeticError("infinitely many solutions")


def parse_user_input(coefficients):
    coefficients = coefficients.split()
    if len(coefficients) != 3:
        raise ValueError("less than three arguments")
    elif any(not is_float_number(i) for i in coefficients):
        raise ValueError("a non-real number is entered")
    return tuple((float(i) for i in coefficients))


def is_float_number(coefficient):
    try:
        float(coefficient)
        return True
    except ValueError:
        return False


def main_func():
    arguments = input("enter three real numbers a, b, c: ")
    try:
        arguments = parse_user_input(arguments)
        print(f"solution:", *solve_equations(*arguments))
    except ValueError as e:
        print(str(e))
    except ArithmeticError as e:
        print(str(e))
    except:
        print("something went wrong, try again later")


if __name__ == "__main__":
    main_func()
