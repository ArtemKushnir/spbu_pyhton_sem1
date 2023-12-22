import warnings
from src.Tests.test_2.safe_call import safe_call, parse_traceback, make_message
import pytest


@safe_call
def foo1(a, b):
    print(a + b)


@safe_call
def foo2(a, b):
    return a / b


@pytest.mark.parametrize(
    "a,b,expected1, expected2",
    [
        (1, 1, "2\n", 1),
        ("a", "f", "af\n", None),
        ([1, 2, 3], [4, 5], "[1, 2, 3, 4, 5]\n", None),
        (4, 2, "6\n", 2),
        (3, 0, "3\n", None),
    ],
)
def test_correct_safe_calls(capfd, a, b, expected1, expected2):
    foo1(a, b)
    output = capfd.readouterr()[0]
    actual = foo2(a, b)
    assert output == expected1
    assert actual == expected2


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (
            1,
            "g",
            "\nfunction name: foo1\n"
            "error type: TypeError\n"
            "error message: unsupported operand type(s) for +: 'int' and 'str'\n"
            "error line: print(a + b)\n"
            "number error line: 8",
        ),
        (
            "abcd",
            [1, 2, 3],
            "\nfunction name: foo1\n"
            "error type: TypeError\n"
            'error message: can only concatenate str (not "list") to str\n'
            "error line: print(a + b)\n"
            "number error line: 8",
        ),
    ],
)
def test_safe_calls_warning(a, b, expected):
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        foo1(a, b)
        assert len(w) == 1
        assert issubclass(w[-1].category, Warning)
        assert expected == str(w[-1].message)


@pytest.mark.parametrize(
    "expected,func,a,b",
    [
        (
            (
                "foo1",
                "TypeError",
                TypeError("unsupported operand type(s) for +: 'int' and 'str'"),
                "print(a + b)",
                17,
            ),
            foo1,
            3,
            "5",
        ),
        (
            (
                "foo2",
                "ZeroDivisionError",
                ZeroDivisionError("division by zero"),
                "return a / b",
                21,
            ),
            foo2,
            5,
            0,
        ),
    ],
)
def test_parse_traceback(expected, func, a, b):
    try:
        func(a, b)
    except Exception:
        actual = parse_traceback()
        assert actual == expected


@pytest.mark.parametrize(
    "output_args,expected",
    [
        (
            [
                "goo",
                "TypeError",
                "unsupported operand type(s) for +: 'int' and 'str'",
                "print(a + b)",
                "333",
            ],
            "\nfunction name: goo\n"
            "error type: TypeError\n"
            "error message: unsupported operand type(s) for +: 'int' and 'str'\n"
            "error line: print(a + b)\n"
            "number error line: 333",
        ),
        (
            [
                "pass_exam",
                "ValueError",
                "i dont pass exam:(",
                "i am taking exam()",
                "666",
            ],
            "\nfunction name: pass_exam\n"
            "error type: ValueError\n"
            "error message: i dont pass exam:(\n"
            "error line: i am taking exam()\n"
            "number error line: 666",
        ),
    ],
)
def test_make_message(output_args, expected):
    actual = make_message(output_args)
    assert actual == expected
