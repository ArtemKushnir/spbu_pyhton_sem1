from src.practice.practice_10 import main_module
import pytest
from io import StringIO


@pytest.mark.parametrize(
    "user_input,expected",
    [
        (
            "5",
            "5 =:\n"
            "START\n"
            "....T\n"
            "........TOKEN\n"
            "............id(5)\n"
            "........PROD\n"
            "............eps\n"
            "....SUM\n"
            "........eps\n",
        ),
        (
            "5 + 3 * 8",
            "5 + 3 * 8 =:\n"
            "START\n"
            "....T\n"
            "........TOKEN\n"
            "............id(5)\n"
            "........PROD\n"
            "............eps\n"
            "....SUM\n"
            "........+\n"
            "........T\n"
            "............TOKEN\n"
            "................id(3)\n"
            "............PROD\n"
            "................*\n"
            "................TOKEN\n"
            "....................id(8)\n"
            "................PROD\n"
            "....................eps\n"
            "........SUM\n"
            "............eps\n",
        ),
        ("55 + + 4", "At the 3 position was expected digit\n"),
        ("( 5 + 3 * 8", "At the 7 position was expected ')'\n"),
        ("5 5", "At the 2 position was expected '+' or '*'\n"),
    ],
)
def test_main_scenario(monkeypatch, user_input, expected):
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main_module.main()
    output = fake_output.getvalue()
    assert output == expected
