from dataclasses import dataclass
from collections import namedtuple
from typing import Any

StackElement = namedtuple("StackElement", ["value", "next"])


@dataclass
class Stack:
    size: int = 0
    head: StackElement = None


def empty(stack: Stack) -> bool:
    return stack.size == 0


def size(stack: Stack) -> int:
    return stack.size


def top(stack: Stack) -> Any:
    if not empty(stack):
        return stack.head.value


def push(stack: Stack, value: Any) -> None:
    new_element = StackElement(value, stack.head)
    stack.head = new_element
    stack.size += 1


def pop(stack: Stack) -> None:
    if not empty(stack):
        stack.head = stack.head.next
        stack.size -= 1


def create_stack():
    return Stack()


if __name__ == "__main__":
    stack1 = create_stack()
    print(top(stack1))
    for i in range(3):
        elem = int(input())
        push(stack1, elem)
    print(empty(stack1))
    print(top(stack1))
    pop(stack1)
    print(top(stack1))
    print(size(stack1))
    pop(stack1)
    print(stack1)
