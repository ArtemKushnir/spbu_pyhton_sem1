import deque


if __name__ == "__main__":
    new_deque = deque.create_deque()
    print(deque.is_empty(new_deque))
    print(deque.get_size(new_deque))
    deque.push_front(new_deque, 1)
    deque.push_front(new_deque, 2)
    deque.push_front(new_deque, 5)
    print(new_deque)
    print(deque.pop_back(new_deque))
    deque.push_back(new_deque, 4)
    print(new_deque)
    print(deque.pop_front(new_deque))
    print(deque.get_size(new_deque))
    print(deque.is_empty(new_deque))
    print(new_deque)
