import queue


if __name__ == "__main__":
    new_queue = queue.create_queue()
    print(queue.is_empty(new_queue))
    queue.push(new_queue, 1)
    queue.push(new_queue, 3)
    queue.push(new_queue, 5)
    print(new_queue)
    print(queue.is_empty(new_queue))
    print(queue.get_top(new_queue))
    queue.pop(new_queue)
    print(queue.get_top(new_queue))
    print(queue.get_size(new_queue))
    print(new_queue)
