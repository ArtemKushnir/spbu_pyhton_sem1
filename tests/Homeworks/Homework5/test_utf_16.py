from src.Homeworks.Homework5 import utf_16
import pytest
from io import StringIO


@pytest.mark.parametrize(
    "string,expected",
    [("aBDHFJ", 2), ("йОГА", 2), ("^", 2), ("🐉qwerty", 4), ("🦔", 4), ("🀑", 4)],
)
def test_get_size(string, expected):
    actual = utf_16.get_size(string)
    assert actual == expected


@pytest.mark.parametrize(
    "string,size,expected",
    [
        ("H", 2, [("H", "U+0048", "00000000 01001000")]),
        ("Й", 2, [("Й", "U+0419", "00000100 00011001")]),
        ("🅰", 4, [("🅰", "U+1F170", "11011000 00111100 11011101 01110000")]),
        ("🏀", 4, [("🏀", "U+1F3C0", "11011000 00111100 11011111 11000000")]),
    ],
)
def test_encode(string, size, expected):
    actual = utf_16.encode(string, size)
    assert actual == expected


@pytest.mark.parametrize(
    "symbol, expected",
    [
        ("J", "00000000000000000000000001001010"),
        ("Ъ", "00000000000000000000010000101010"),
        ("💣", "11011000001111011101110010100011"),
        ("💔", "11011000001111011101110010010100"),
    ],
)
def test_encode_binary_4_byte(symbol, expected):
    actual = utf_16.encode_binary_4_byte(symbol)
    assert actual == expected


@pytest.mark.parametrize(
    "user_input,expected",
    [
        (
            "Hello",
            "H\tU+0048\t00000000 01001000\n"
            "e\tU+0065\t00000000 01100101\n"
            "l\tU+006C\t00000000 01101100\n"
            "l\tU+006C\t00000000 01101100\n"
            "o\tU+006F\t00000000 01101111\n",
        )
    ],
)
def test_main_scenario(monkeypatch, user_input, expected):
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    fake_output = StringIO()
    utf_16.main()
    monkeypatch.setattr("sys.stdout", fake_output)
    utf_16.main()
    output = fake_output.getvalue()
    assert output == expected
