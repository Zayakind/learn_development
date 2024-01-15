from typing import Any


class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val: Any) -> Node | None:
        if self.head is None:
            return None
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val: Any) -> list:
        found_values = []
        if self.head is None:
            return found_values
        node = self.head
        while node is not None:
            if node.value == val:
                found_values.append(node)
            node = node.next
        return found_values

    def delete(self, val: Any, all=False) -> None:
        if self.head is None:
            return None
        if self.head.next is None:
            if self.head.value == val:
                self.head = None
                self.tail = None
                return
        if self.head.value == val:
            self.head = self.head.next
            self.head.prev = None
            return
        if self.tail.value == val:
            self.tail = self.tail.prev
            self.tail.next = None
            return
        node = self.head
        while node:
            if node.value == val:
                node.prev.next = node.next
                if node.next:
                    node.next.prev = node.prev
                if not all:
                    return
            node = node.next

    def insert(self, after_node: Node | None, new_node: Node) -> None:
        if after_node is None:
            self.add_in_tail(new_node)
            return
        if after_node is self.tail:
            self.add_in_tail(new_node)
            return
        new_node.prev = after_node
        new_node.next = after_node.next
        after_node.next.prev = new_node
        after_node.next = new_node

    def add_in_head(self, new_node: Node) -> None:
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def clean(self) -> None:
        self.head = None
        self.tail = None

    def len(self) -> int | None:
        if self.head is None:
            return 0
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result
