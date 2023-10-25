from Queue import *


if __name__ == "__main__":
    new_queue = create_queue()
    print(empty(new_queue))  # False
    push(new_queue, 1)  # add 1
    push(new_queue, 3)  # add 3
    push(new_queue, 5)  # add 5
    print(empty(new_queue))  # True
    print(top(new_queue))  # 1
    pop(new_queue)  # delete 1
    print(top(new_queue))  # 3
    print(new_queue)
