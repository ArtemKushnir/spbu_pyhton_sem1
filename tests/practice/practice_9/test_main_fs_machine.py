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
        (
            "abb\nend",
            "Enter a word to determine which language it belongs to or enter the 'end' to finish the job: "
            "This word belongs to the language '(a|b)*abb'\n"
            "Enter a word to determine which language it belongs to or enter the 'end' to finish the job: ",
        ),
        (
            "abb\n12.123E+23\nend",
            "Enter a word to determine which language it belongs to or enter the 'end' to finish "
            "the job: "
            "This word belongs to the language '(a|b)*abb'\n"
            "Enter a word to determine which language it belongs to or enter the 'end' to finish "
            "the job: "
            "This word belongs to the language 'digit+(.digit+)?(E(+|-)?digit+)?'\n"
            "Enter a word to determine which language it belongs to or enter the 'end' to finish "
            "the job: ",
        ),
        (
            "bbab\nend",
            "Enter a word to determine which language it belongs to or enter the 'end' to finish the job: "
            "There was no suitable language\n"
            "Enter a word to determine which language it belongs to or enter the 'end' to finish the job: ",
        ),
    ],
)
def test_main_scenario(monkeypatch, user_input, expected):
    arguments = StringIO(user_input)
    monkeypatch.setattr("sys.stdin", arguments)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main_fs_machine.main()
    output = fake_output.getvalue()
    assert output == expected
