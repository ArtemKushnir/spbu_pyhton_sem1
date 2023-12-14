from dataclasses import dataclass


@dataclass
class FSMachine:
    table_states: dict[int, dict[str, int]]
    initial_state: int
    terminal_states: set[int]


def _switch_to_new_state(curr_symbol: str, state: int, fsm: FSMachine) -> int | None:
    for key, value in fsm.table_states[state].items():
        if curr_symbol in key:
            return value


def create_fs_machine(
    states: dict[int, dict[str, int]], initial_state: int, terminal_states: set[int]
) -> FSMachine:
    return FSMachine(states, initial_state, terminal_states)


def validate_string(fsm: FSMachine, string: str) -> bool:
    current_state = fsm.initial_state
    for i in string:
        current_state = _switch_to_new_state(i, current_state, fsm)
        if current_state is None:
            return False
    return current_state in fsm.terminal_states
