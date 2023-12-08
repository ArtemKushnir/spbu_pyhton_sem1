from dataclasses import dataclass
from typing import Callable


@dataclass
class FSMachine:
    table_states: dict[int, dict[str, int]]
    move: Callable[[str, int, "FSMachine"], int]
    initial_state: int
    final_states: set[int]


def _switch_to_new_state(curr_symbol: str, state: int, fsm: FSMachine) -> int | None:
    return fsm.table_states[state].get(curr_symbol)


def create_fs_machine(
    states: dict[int, dict[str, int]], initial_state: int, final_states: set[int]
) -> FSMachine:
    return FSMachine(states, _switch_to_new_state, initial_state, final_states)


def validate_string(fsm: FSMachine, string: str) -> bool:
    current_state = fsm.initial_state
    for i in string:
        current_state = fsm.move(i, current_state, fsm)
        if current_state is None:
            return False
    if current_state in fsm.final_states:
        return True
    return False
