from src.practice.practice_6.task_1 import *
from io import StringIO
import pytest


test_raise_exception_quadratic_equation_array = [
    (100, 5, 2.9),
    (10, 1, 2),
    (-10, 20, -40),
]

test_quadratic_equation_two_roots_array = [
    (2, -1, -15, (3, -2.5)),
    (-1, 2, 3, (-1, 3)),
    (5, 6, 1, (-1, -0.2)),
]

test_quadratic_equation_one_roots_array = [
    (1, 8, 16, (-4,)),
    (-25, 20, -4, (0.4,)),
    (1, 4, 4, (-2,)),
]

test_linear_equation_array = [(50, -100, 2), (10.5, 105, -10), (-4, -62, -15.5)]

test_raise_exception_validation_user_input_array = [
    ["0", "5"],
    ["d", "5", "l"],
    ["", "", ""],
]

test_main_scenario_array = [
    ("2 -1 -15", "roots of quadratic equation: -2.5, 3.0"),
    ("1 8 16", "root of quadratic equation: -4.0"),
    ("10 1 3", "To find real roots discriminant must be non-negative"),
    ("0 20 40", "root of a linear equation: -2.0"),
    ("0 0 0", "infinitely many solutions"),
    ("0 0 5", "no solutions"),
]


@pytest.mark.parametrize("a,b,c", test_raise_exception_quadratic_equation_array)
def test_raise_exception_quadratic_equation(a, b, c):
    with pytest.raises(ArithmeticError):
        solve_quadratic_equation(a, b, c)


@pytest.mark.parametrize("a,b,c,expected", test_quadratic_equation_two_roots_array)
def test_quadratic_equation_two_roots(a, b, c, expected):
    actual = solve_quadratic_equation(a, b, c)
    assert (actual[0] == expected[0] and actual[1] == expected[1]) or (
        actual[1] == expected[0] and actual[0] == expected[1]
    )


@pytest.mark.parametrize("a,b,c,expected", test_quadratic_equation_one_roots_array)
def test_quadratic_equation_one_roots(a, b, c, expected):
    actual = solve_quadratic_equation(a, b, c)
    assert actual[0] == expected[0]


@pytest.mark.parametrize("b,c,expected", test_linear_equation_array)
def test_linear_equation(b, c, expected):
    actual = solve_linear_equation(b, c)
    assert actual == expected


def test_raise_exception_linear_equation():
    with pytest.raises(ArithmeticError):
        solve_constant_equation(78)


def test_constant_equation():
    assert solve_constant_equation(0) == float("inf")


def test_is_float_number():
    assert is_float_number(["2.5", "3", "-4.5"]) == [2.5, 3, -4.5]


def test_raise_exception_is_float_number():
    with pytest.raises(ValueError):
        is_float_number(["1", "2", "f"])


def test_validation_user_input():
    assert validation_user_input(["0", "-99.9", "45.46"]) == [0, -99.9, 45.46]


@pytest.mark.parametrize(
    "coefficients", test_raise_exception_validation_user_input_array
)
def test_raise_exception_validation_user_input(coefficients):
    with pytest.raises(ValueError):
        validation_user_input(coefficients)


def test_determine_type_quadratic_equation():
    actual_2_roots = determine_type_equation(2, -1, -15)
    actual_1_roots = determine_type_equation(1, 8, 16)
    assert actual_2_roots == "roots of quadratic equation: -2.5, 3.0"
    assert actual_1_roots == "root of quadratic equation: -4.0"


def test_determine_type_linear_equation():
    actual = determine_type_equation(0, 50, -100)
    assert actual == "root of a linear equation: 2.0"


def test_determine_type_constant_equation():
    actual = determine_type_equation(0, 0, 0)
    assert actual == "infinitely many solutions"


@pytest.mark.parametrize("user_input,expected", test_main_scenario_array)
def test_main_scenario(monkeypatch, user_input, expected):
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    fake_output = StringIO(main_func())
    monkeypatch.setattr("sys.stdout", fake_output)
    output = fake_output.getvalue()
    assert output == expected
