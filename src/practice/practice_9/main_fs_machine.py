from src.practice.practice_9 import fsm
import string


LANGUAGES = ["(a|b)*abb", "digit+(.digit+)?(E(+|-)?digit+)?"]


def create_correct_fsm(name_language: str) -> fsm.FSMachine:
    if name_language == LANGUAGES[0]:
        states = {
            0: {"b": 0, "a": 1},
            1: {"a": 1, "b": 2},
            2: {"a": 1, "b": 3},
            3: {"b": 0, "a": 1},
        }
        initial_state = 0
        terminal_states = {3}
    elif name_language == LANGUAGES[1]:
        states = {
            0: {string.digits: 1},
            1: {".": 2, "E": 4, string.digits: 1},
            2: {string.digits: 3},
            3: {"E": 4, string.digits: 3},
            4: {"+-": 5, string.digits: 6},
            5: {string.digits: 6},
            6: {string.digits: 6},
        }
        initial_state = 0
        terminal_states = {1, 3, 6}
    return fsm.create_fs_machine(states, initial_state, terminal_states)


def main() -> None:
    fs_machines = []
    for language in LANGUAGES:
        fs_machines.append(create_correct_fsm(language))
    input_word = input(
        "Enter a word to determine which language it belongs to or enter the 'end' to finish the job: "
    )
    while input_word != "end":
        for i in range(len(fs_machines)):
            if fsm.validate_string(fs_machines[i], input_word):
                print(f"This word belongs to the language '{LANGUAGES[i]}'")
                break
        else:
            print("There was no suitable language")
        input_word = input(
            "Enter a word to determine which language it belongs to or enter the 'end' to finish the "
            "job: "
        )


if __name__ == "__main__":
    main()
