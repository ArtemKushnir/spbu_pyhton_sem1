from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class QueueNode:
    value: Any
    next: Optional["QueueNode"]


@dataclass
class Queue:
    size: int
    head: Optional[QueueNode]
    last_node: Optional[QueueNode]


def is_empty(queue: Queue) -> bool:
    return queue.size == 0


def get_size(queue: Queue) -> int:
    return queue.size


def get_top(queue: Queue) -> Any:
    if not is_empty(queue):
        return queue.head.value


def push(queue: Queue, value: Any) -> None:
    new_element = QueueNode(value, None)
    if is_empty(queue):
        queue.head = new_element
        queue.last_node = new_element
        queue.size += 1
    else:
        queue.last_node.next = new_element
        queue.last_node = new_element
        queue.size += 1


def pop(queue: Queue) -> None:
    if not is_empty(queue):
        queue.head = queue.head.next
        queue.size -= 1


def create_queue() -> Queue:
    return Queue(0, None, None)
