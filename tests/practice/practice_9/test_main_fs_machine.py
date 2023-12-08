from src.practice.practice_9 import main_fs_machine, fsm
from io import StringIO
import pytest


def test_create_correct_fs_machine():
    actual = main_fs_machine.create_correct_fsm(main_fs_machine.LANGUAGES[0])
    states = {
        0: {"b": 0, "a": 1},
        1: {"a": 1, "b": 2},
        2: {"a": 1, "b": 3},
        3: {"b": 0, "a": 1},
    }
    expected = fsm.create_fs_machine(states, 0, {3})
    assert actual == expected


@pytest.mark.parametrize(
    "user_input,expected",
    [
        ("abb", "This word belongs to the language '(a|b)*abb'\n"),
        ("aaaaaababb", "This word belongs to the language '(a|b)*abb'\n"),
        ("bbbbabb", "This word belongs to the language '(a|b)*abb'\n"),
        ("bbab", "There was no suitable language\n"),
        ("cb", "There was no suitable language\n"),
    ],
)
def test_main_scenario(monkeypatch, user_input, expected):
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main_fs_machine.main()
    output = fake_output.getvalue()
    assert output == expected
