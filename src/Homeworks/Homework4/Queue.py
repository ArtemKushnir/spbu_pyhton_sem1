from dataclasses import dataclass


@dataclass
class Queue:
    size: int = 0
    head: dict = None
    tail: dict = None


def empty(queue: Queue) -> bool:
    return queue.size == 0


def size(queue: Queue) -> int:
    return queue.size


def top(queue: Queue) -> any:
    if not empty(queue):
        return queue.head["value"]


def push(queue: Queue, value: any) -> any:
    new_element = {"value": value, "next": None}
    if empty(queue):
        queue.head = new_element
        queue.tail = new_element
    else:
        queue.tail["next"] = new_element
        queue.tail = new_element
    queue.size += 1


def pop(queue: Queue) -> any:
    if not empty(queue):
        queue.head = queue.head["next"]
        queue.size -= 1


def create_queue() -> any:
    return Queue()
