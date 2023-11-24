from src.Tests.test_2 import fibonacci
import pytest
from io import StringIO


@pytest.mark.parametrize(
    "n, expected", [(0, 0), (90, 2880067194370816120), (1, 1), (2, 1), (25, 75025)]
)
def test_get_fibonacci_number(n, expected):
    actual = fibonacci.get_fibonacci_number(n)
    assert actual == expected


@pytest.mark.parametrize("n,expected", [("0", 0), ("90", 90), ("59", 59)])
def test_validate_input(n, expected):
    actual = fibonacci.validate_input(n)
    assert actual == expected


@pytest.mark.parametrize("n", ["a", "1.4", "-1", "99"])
def test_raise_exception_validate_input(n):
    with pytest.raises(ValueError):
        fibonacci.validate_input(n)


@pytest.mark.parametrize(
    "user_input,expected",
    [
        ("0", "fibonacci number number 0 = 0\n"),
        ("90", "fibonacci number number 90 = 2880067194370816120\n"),
        ("a", "it's not an integer\n"),
        ("105", "wrong number\n"),
    ],
)
def test_main_scenario(monkeypatch, user_input, expected):
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    fake_output = StringIO()
    fibonacci.main()
    monkeypatch.setattr("sys.stdout", fake_output)
    fibonacci.main()
    output = fake_output.getvalue()
    assert output == expected
