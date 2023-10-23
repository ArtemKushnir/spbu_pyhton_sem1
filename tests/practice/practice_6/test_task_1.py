from src.practice.practice_6.task_1 import *
from io import StringIO
import pytest


@pytest.mark.parametrize("a,b,c", [(100, 5, 2.9), (10, 1, 2), (-10, 20, -40)])
def test_raise_exception_quadratic_equation(a, b, c):
    with pytest.raises(ArithmeticError):
        solve_quadratic_equation(a, b, c)


@pytest.mark.parametrize(
    "a,b,c,expected",
    [(2, -1, -15, (3, -2.5)), (-1, 2, 3, (-1, 3)), (5, 6, 1, (-1, -0.2))],
)
def test_quadratic_equation_two_roots(a, b, c, expected):
    actual = solve_quadratic_equation(a, b, c)
    assert (actual[0] == expected[0] and actual[1] == expected[1]) or (
        actual[1] == expected[0] and actual[0] == expected[1]
    )


@pytest.mark.parametrize(
    "a,b,c,expected", [(1, 8, 16, (-4,)), (-25, 20, -4, (0.4,)), (1, 4, 4, (-2,))]
)
def test_quadratic_equation_one_roots(a, b, c, expected):
    actual = solve_quadratic_equation(a, b, c)
    assert actual[0] == expected[0]


@pytest.mark.parametrize(
    "b,c,expected", [(50, -100, 2), (10.5, 105, -10), (-4, -62, -15.5)]
)
def test_linear_equation(b, c, expected):
    actual = solve_linear_equation(b, c)
    assert actual == expected


@pytest.mark.parametrize("c", [1, 0.5, -99.9])
def test_raise_exception_constant_equation(c):
    with pytest.raises(ArithmeticError):
        solve_constant_equation(c)


def test_constant_equation():
    assert solve_constant_equation(0) == float("inf")


@pytest.mark.parametrize(
    "coefficients,expected",
    [
        (("2.5", "3", "-4.5"), (2.5, 3, -4.5)),
        (("-1", "0", "0"), (-1, 0, 0)),
        (("0", "-128", "8.8"), (0, -128, 8.8)),
    ],
)
def test_is_float_number(coefficients, expected):
    assert is_float_number(coefficients) == expected


@pytest.mark.parametrize(
    "coefficients", [["1", "2", "f"], ["1..5", "2", "3"], ["1,5", "3", "6,7"]]
)
def test_raise_exception_is_float_number(coefficients):
    with pytest.raises(ValueError):
        is_float_number(coefficients)


@pytest.mark.parametrize(
    "coefficients, expected",
    [
        (("0", "-99.9", "45.56"), (0.0, -99.9, 45.56)),
        (("123", "0.9", "1"), (123.0, 0.9, 1.0)),
        (("1.1", "2.3", "456.9"), (1.1, 2.3, 456.9)),
    ],
)
def test_validation_user_input(coefficients, expected):
    assert validation_user_input(coefficients) == expected


@pytest.mark.parametrize("coefficients", [["0", "5"], ["d", "5", "l"], ["", "", ""]])
def test_raise_exception_validation_user_input(coefficients):
    with pytest.raises(ValueError):
        validation_user_input(coefficients)


@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        (2, -1, -15, "roots of quadratic equation: -2.5, 3.0"),
        (1, 8, 16, "root of quadratic equation: -4.0"),
    ],
)
def test_determine_type_quadratic_equation(a, b, c, expected):
    assert determine_type_equation(a, b, c) == expected


@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        (0, 50, -100, "root of a linear equation: 2.0"),
        (0, 20, 10, "root of a linear equation: -0.5"),
        (0, 1000, -10, "root of a linear equation: 0.01"),
    ],
)
def test_determine_type_linear_equation(a, b, c, expected):
    assert determine_type_equation(a, b, c) == expected


def test_determine_type_constant_equation():
    actual = determine_type_equation(0, 0, 0)
    assert actual == "infinitely many solutions"


@pytest.mark.parametrize(
    "user_input,expected",
    [
        ("2 -1 -15", "roots of quadratic equation: -2.5, 3.0"),
        ("1 8 16", "root of quadratic equation: -4.0"),
        ("10 1 3", "To find real roots discriminant must be non-negative"),
        ("0 20 40", "root of a linear equation: -2.0"),
        ("0 0 0", "infinitely many solutions"),
        ("0 0 5", "no solutions"),
    ],
)
def test_main_scenario(monkeypatch, user_input, expected):
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    fake_output = StringIO(main_func())
    monkeypatch.setattr("sys.stdout", fake_output)
    output = fake_output.getvalue()
    assert output == expected
