from . import fsm


LANGUAGES = ["(a|b)*abb"]


def create_correct_fsm(name_language: str) -> fsm.FSMachine:
    if name_language == LANGUAGES[0]:
        states = {
            0: {"b": 0, "a": 1},
            1: {"a": 1, "b": 2},
            2: {"a": 1, "b": 3},
            3: {"b": 0, "a": 1},
        }
        initial_state = 0
        final_states = {3}
    return fsm.create_fs_machine(states, initial_state, final_states)


def main() -> None:
    input_word = input("Enter a word to determine which language it belongs to: ")
    for language in LANGUAGES:
        new_fsm = create_correct_fsm(language)
        if fsm.validate_string(new_fsm, input_word):
            print(f"This word belongs to the language '{language}'")
            break
    else:
        print("There was no suitable language")


if __name__ == "__main__":
    main()
