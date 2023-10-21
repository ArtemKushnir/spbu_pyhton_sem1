def determine_type_equation(a, b, c):
    if a != 0:
        roots = solve_quadratic_equation(a, b, c)
        if len(roots) == 2:
            return f"roots of quadratic equation: {min(roots)}, {max(roots)}"
        else:
            return f"root of quadratic equation: {roots[0]}"
    elif b != 0:
        return f"root of a linear equation: {solve_linear_equation(b, c)}"
    else:
        if solve_constant_equation(c):
            return "infinitely many solutions"


def solve_quadratic_equation(a, b, c):
    d = b**2 - 4 * a * c
    if d == 0:
        return [-b / (2 * a)]
    elif d > 0:
        return [(-b + d**0.5) / (2 * a), (-b - d**0.5) / (2 * a)]
    raise ArithmeticError("To find real roots discriminant must be non-negative")


def solve_linear_equation(b, c):
    return -c / b


def solve_constant_equation(c):
    if c != 0:
        raise ArithmeticError("no solutions")
    return float("inf")


def validation_user_input(coefficients):
    if len(coefficients) != 3:
        raise ValueError("less than three arguments")
    try:
        return is_float_number(coefficients)
    except ValueError as e:
        raise e


def is_float_number(coefficients):
    try:
        return [float(i) for i in coefficients]
    except ValueError:
        raise ValueError("is not a real number")


def main_func():
    arguments = input("enter three real numbers a, b, c: ").split()
    try:
        arguments = validation_user_input(arguments)
    except ValueError as e:
        return str(e)
    try:
        return determine_type_equation(*arguments)
    except ArithmeticError as e:
        return str(e)


if __name__ == "__main__":
    print(main_func())
