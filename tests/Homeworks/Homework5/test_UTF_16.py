from src.Homeworks.Homework5.UTF_16 import *
import pytest


@pytest.mark.parametrize(
    "string,expected", [("a", 2), ("Й", 2), ("^", 2), ("🐉", 4), ("🦔", 4), ("🀑", 4)]
)
def test_get_size(string, expected):
    actual = get_size(string)
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
    actual = encode(string, size)
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
    actual = encode_binary_4_byte(symbol)
    assert actual == expected
