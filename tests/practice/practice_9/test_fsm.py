import pytest
from src.practice.practice_9 import fsm


@pytest.mark.parametrize(
    "states,initial_state,final_states",
    [
        (
            {
                0: {"b": 0, "a": 1},
                1: {"a": 1, "b": 2},
                2: {"a": 1, "b": 3},
                3: {"b": 0, "a": 1},
            },
            0,
            {3},
        ),
        ({0: {"a": 3, "b": 1, "c": 4, "z": 2}}, 0, {1, 2, 3, 4}),
        ({0: {"a": 1}, 1: {"b": 2}, 2: {"c": 3}, 3: {"d": 4}}, 0, {4}),
    ],
)
def test_create_fs_machine(states, initial_state, final_states):
    dummy_fsm = fsm.FSMachine(
        states, fsm._switch_to_new_state, initial_state, final_states
    )
    curr_fsm = fsm.create_fs_machine(states, initial_state, final_states)
    assert dummy_fsm == curr_fsm


@pytest.mark.parametrize(
    "string,expected",
    [
        ("aaaabb", True),
        ("abb", True),
        ("bbbabb", True),
        ("abbb", False),
        ("abba", False),
        ("cabb", False),
    ],
)
def test_validate_string(string, expected):
    states = {
        0: {"b": 0, "a": 1},
        1: {"a": 1, "b": 2},
        2: {"a": 1, "b": 3},
        3: {"b": 0, "a": 1},
    }
    dummy_fsm = fsm.create_fs_machine(states, 0, {3})
    actual = fsm.validate_string(dummy_fsm, string)
    assert actual == expected


@pytest.mark.parametrize(
    "symbol,state,expected",
    [("b", 0, 0), ("a", 0, 1), ("b", 3, 0), ("c", 0, None), ("d", 3, None)],
)
def test_switch_to_new_state(symbol, state, expected):
    states = {
        0: {"b": 0, "a": 1},
        1: {"a": 1, "b": 2},
        2: {"a": 1, "b": 3},
        3: {"b": 0, "a": 1},
    }
    dummy_fsm = fsm.create_fs_machine(states, 0, {3})
    actual = fsm._switch_to_new_state(symbol, state, dummy_fsm)
    assert actual == expected
