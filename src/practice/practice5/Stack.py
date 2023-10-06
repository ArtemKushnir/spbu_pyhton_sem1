from dataclasses import dataclass
from collections import namedtuple


StackElement = namedtuple(
    "StackElement", ["value", "next"]
)


@dataclass
class Stack:
    size: int
    head: StackElement = None


def empty(stack: Stack) -> bool:
    return stack.size == 0


def size(stack: Stack) -> int:
    return stack.size


def top(stack: Stack) -> any:
    if stack.size != 0:
        return stack.head.value


def push(stack: Stack, value: any) -> None:
    new_element = StackElement(value, stack.head)
    stack.head = new_element
    stack.size += 1


def pop(stack: Stack) -> None:
    stack.head = stack.head.next
    stack.size -= 1


if __name__ == "__main__":
    stack1 = Stack(0)
    print(top(stack1))
    for i in range(3):
        elem = int(input())
        push(stack1, elem)
    print(empty(stack1))
    print(top(stack1))
    pop(stack1)
    print(top(stack1))
    print(size(stack1))
    