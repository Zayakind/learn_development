from typing import Any


class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, entry: Any) -> None:
        self.items.append(entry)

    def dequeue(self) -> Any:
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def size(self) -> int:
        size = 0
        for _ in self.items:
            size += 1
        return size


def split_queue(count: int, queue: Queue) -> None:
    for i in range(count):
        split = queue.dequeue()
        queue.enqueue(split)
