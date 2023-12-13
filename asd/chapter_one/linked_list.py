from typing import Any


class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item: Node) -> None:
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self) -> None:
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val: Any) -> Node | None:
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val: Any) -> list[Node] | None:
        result = []
        node = self.head
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next
        if result is None or result == []:
            return None
        return result

    def delete(self, val: Any, all=False) -> None:
        current = self.head
        prev = None
        while current:
            if current.value == val:
                if current == self.head:
                    self.head = current.next
                    if self.tail == self.head:
                        self.tail = current.next
                else:
                    prev.next = current.next
                if current == self.tail:
                    self.tail = prev
                if not all:
                    return
            else:
                prev = current
            current = current.next

    def clean(self) -> None:
        self.head = None
        self.tail = None

    def len(self) -> int | None:
        if self.head is None:
            return 0
        result = 0
        node = self.head
        while node is not None:
            result += 1
            node = node.next
        return result

    def insert(self, after_node: Node | None, new_node: Node) -> None:
        if after_node is None:
            new_node.next = self.head
            self.head = new_node
            return
        new_node.next, after_node.next = after_node.next, new_node


def sum_linked_lists(one: LinkedList, two: LinkedList) -> LinkedList | None:
    if one.len() != two.len():
        return None
    result = LinkedList()
    current_1 = one.head
    current_2 = two.head
    while current_1 is not None and current_2 is not None:
        result.add_in_tail(Node(current_1.value + current_2.value))
        current_1 = current_1.next
        current_2 = current_2.next
    return result
