from src.Homeworks.homework_6 import avl_tree
from os.path import exists


def process_add_request(
    tree: avl_tree.Tree[avl_tree.Value], key: int, value: int
) -> None:
    if not avl_tree.has_key(tree, key):
        avl_tree.put(tree, key, value)
    else:
        old_value = avl_tree.get(tree, key)
        avl_tree.put(tree, key, value + old_value)


def process_get_request(tree: avl_tree.Tree[avl_tree.Value], key: int) -> int:
    if not avl_tree.has_key(tree, key):
        return 0
    return avl_tree.get(tree, key)


def process_select_request(tree: avl_tree.Tree[avl_tree.Value], key: int) -> str | int:
    try:
        result_key = avl_tree.get_lower_bound(tree, key)
        old_value = avl_tree.get(tree, result_key)
        if old_value == 1:
            avl_tree.remove(tree, result_key)
        else:
            avl_tree.put(tree, result_key, old_value - 1)
        return result_key
    except ValueError:
        return "there is no suitable size"


def process_request(
    tree: avl_tree.Tree[avl_tree.Value], curr_request: str
) -> str | int:
    action, *argument = curr_request.split()
    argument = list(map(int, argument))
    if action == "ADD":
        process_add_request(tree, *argument)
        return "instances added"
    elif action == "GET":
        return process_get_request(tree, argument[0])
    else:
        return process_select_request(tree, argument[0])


def validate_request(curr_request: str) -> bool:
    action, *argument = curr_request.split()
    if action == "ADD" and len(argument) == 2:
        if argument[0].lstrip("-").isdigit() and argument[1].lstrip("-").isdigit():
            return True
    elif action == "GET" and len(argument) == 1:
        if argument[0].isdigit():
            return True
    elif action == "SELECT" and len(argument) == 1:
        if argument[0].isdigit():
            return True
    return False


def process_input_file(
    tree: avl_tree.Tree[avl_tree.Value], read_file_name: str
) -> list[str]:
    results = []
    with open(read_file_name) as file:
        for string in file:
            if "ADD" in string:
                process_request(tree, string)
            else:
                results.append(process_request(tree, string))
    return results


def write_results(result_file_name: str, results: list) -> None:
    string_results = "\n".join([str(i) for i in results])
    with open(result_file_name, "w") as file:
        file.write(string_results)


def calculate_and_write_remains(
    tree: avl_tree.Tree[avl_tree.Value], leftover_file_name: str
) -> None:
    remains = avl_tree.traverse(tree, "inorder")
    result = ""
    for element in remains:
        result += (
            str(element.key).center(4) + "\t" + str(element.value).center(5) + "\n"
        )
    with open(leftover_file_name, "w") as file:
        file.write("size\tcount\n")
        file.write(result)


def file_check(
    read_file_name: str, result_file_name: str, leftover_file_name: str
) -> bool:
    if not exists(read_file_name):
        print(f"не существует {read_file_name}")
        return False
    if exists(result_file_name):
        print(f"файл {result_file_name} уже существует")
        return False
    if exists(leftover_file_name):
        print(f"файл {leftover_file_name} уже существует")
        return False

    return True


def main():
    selected_action = ""
    new_tree = avl_tree.create_tree()
    while selected_action != "3":
        print("1.Enter a request\n2.Test the program on the given data\n3.Finish work")
        selected_action = input("Select an action: ")
        if selected_action == "1":
            print("enter 'end' to exit the menu")
            request = input("Incoming request: ")
            while request != "end":
                if not validate_request(request):
                    print("wrong request")
                    break
                print(process_request(new_tree, request))
                print("enter 'end' to exit the menu")
                request = input("Incoming request: ")
        elif selected_action == "2":
            test_tree = avl_tree.create_tree()
            read_file = input("Enter the name of the request file: ")
            result_file = input(
                "Enter the name of the file where to record the selected shoes: "
            )
            leftover_file = input(
                "Enter the name of the file where to write the leftovers: "
            )
            if file_check(read_file, result_file, leftover_file):
                results = process_input_file(test_tree, read_file)
                write_results(result_file, results)
                calculate_and_write_remains(test_tree, leftover_file)
        elif selected_action not in "123":
            print("invalid command entered")


if __name__ == "__main__":
    main()
