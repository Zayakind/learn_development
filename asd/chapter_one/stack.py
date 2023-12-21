from typing import Any


class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self) -> Any | None:
        if self.size() > 0:
            return self.stack.pop(0)
        return None

    def push(self, value: Any) -> None:
        return self.stack.insert(0, value)

    def peek(self):
        if self.size() > 0:
            return self.stack[0]
        return None


def parsing_string(string: str) -> bool:
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}'}
    for char in string:
        if char in brackets:
            stack.append(char)
        if char in brackets.values() and (not stack or brackets[stack.pop()] != char):
            return False
    return not stack
