from src.leet_code.zigzag import convert, main
from io import StringIO
import pytest


@pytest.mark.parametrize(
    "string,rows,expected",
    [
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        ("ABCBA", 1, "ABCBA"),
        ("QWERTY", 7, "QWERTY"),
    ],
)
def test_convert(string, rows, expected):
    actual = convert(string, rows)
    assert actual == expected


@pytest.mark.parametrize(
    "user_input,expected",
    [
        (
            "PAYPALISHIRING\n3",
            "Enter string: Enter rows for record string: string after transformations: PAHNAPLSIIGYIR\n",
        ),
        (
            "PAYPALISHIRING\ng",
            "Enter string: Enter rows for record string: rows must be integer\n",
        ),
        (
            "ARTEMKUSHNIR\n7",
            "Enter string: Enter rows for record string: string after transformations: ARRTIENMHKSU\n",
        ),
    ],
)
def test_main_scenario(monkeypatch, expected, user_input):
    monkeypatch.setattr("sys.stdin", StringIO(user_input))
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    output = fake_output.getvalue()
    assert output == expected
