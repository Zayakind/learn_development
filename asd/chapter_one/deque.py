class Deque:
    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.insert(0, item)

    def addTail(self, item):
        self.items.append(item)

    def removeFront(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def removeTail(self):
        if self.size() == 0:
            return None
        return self.items.pop(-1)

    def size(self):
        count = 0
        for _ in self.items:
            count += 1
        return count


def check_palindrome(example: str):
    deque = Deque()
    for letter in example:
        deque.addTail(letter)
    check = []
    for _ in range(len(example) // 2):
        if deque.removeFront() == deque.removeTail() or deque.size() == 1:
            check.append(True)
            continue
        check.append(False)

    return all(check)
