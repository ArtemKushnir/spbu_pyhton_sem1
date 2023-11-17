from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Node:
    value: Any = None
    next: Optional["Node"] = None


@dataclass
class Deque:
    size: int = 0
    head: Optional[Node] = None
    tail: Optional[Node] = None


def create_deque() -> Deque:
    return Deque()


def pop_front(deque: Deque) -> Any:
    if not is_empty(deque):
        first_element = deque.head.value
        deque.head = deque.head.next
        deque.size -= 1
        return first_element


def pop_back(deque: Deque) -> Any:
    if not is_empty(deque):
        if deque.size == 1:
            element = deque.head.value
            deque.head = None
            deque.tail = None
            deque.size -= 1
            return element
        curr_node = deque.head
        previous_element = None
        while curr_node.next is not None:
            previous_element = curr_node
            curr_node = curr_node.next
        previous_element.next = None
        deque.tail = previous_element
        deque.size -= 1
        return curr_node.value


def push_front(deque: Deque, value: Any) -> None:
    new_element = Node(value, None)
    if deque.head is None:
        deque.head = new_element
        deque.size += 1
    else:
        new_element.next = deque.head
        deque.head = new_element
        deque.size += 1


def push_back(deque: Deque, value: Any) -> None:
    new_element = Node(value, None)
    if deque.head is None:
        deque.head = new_element
        deque.tail = new_element
        deque.size += 1
    else:
        deque.tail.next = new_element
        deque.tail = new_element
        deque.size += 1


def get_size(deque: Deque) -> Optional[int]:
    return deque.size


def is_empty(deque: Deque) -> bool:
    return deque.size == 0
