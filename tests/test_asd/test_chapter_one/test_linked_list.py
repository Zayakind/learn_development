from asd.chapter_one.linked_list import Node, LinkedList, sum_linked_lists

import pytest

def create_node(count: int) -> list[Node]:
    return [Node(i+1) for i in range(count)]


def test_delete_is_empty_list():
    linked_list = LinkedList()
    assert not linked_list.delete(1)


def test_find_is_empty_list():
    linked_list = LinkedList()
    assert not linked_list.find(1)


def test_find_all_is_empty_list():
    linked_list = LinkedList()
    assert not linked_list.find_all(1)


def test_delete_is_one_element_list():
    linked_list = LinkedList()
    node_one = Node(1)
    linked_list.add_in_tail(node_one)
    linked_list.delete(1)
    assert linked_list.head is None
    assert linked_list.tail is None


def test_add_tail():
    linked_list = LinkedList()
    node_one = Node(1)
    linked_list.add_in_tail(node_one)
    assert linked_list.head == node_one


def test_print_all_nodes(capsys):
    linked_list = LinkedList()
    linked_list.add_in_tail(Node(1))
    linked_list.add_in_tail(Node(2))
    linked_list.add_in_tail(Node(3))
    linked_list.print_all_nodes()
    assert capsys.readouterr().out.replace("\n", " ").strip() == "1 2 3"


def test_find():
    node_1, node_2, node_3 = create_node(3)
    linked_list = LinkedList()
    linked_list.add_in_tail(node_1)
    linked_list.add_in_tail(node_2)
    linked_list.add_in_tail(node_3)
    assert linked_list.find(2).value == node_2.value


def test_find_all():
    node_1, node_2, node_3 = create_node(3)
    node_4 = Node(2)
    linked_list = LinkedList()
    linked_list.add_in_tail(node_1)
    linked_list.add_in_tail(node_2)
    linked_list.add_in_tail(node_3)
    linked_list.add_in_tail(node_4)
    assert linked_list.find_all(2) == [node_2, node_4]


def test_find_none_value_list():
    linked_list = LinkedList()
    linked_list.add_in_tail(Node(1))
    assert not linked_list.find(5)


def test_find_none_value_all_list():
    linked_list = LinkedList()
    linked_list.add_in_tail(Node(1))
    assert not linked_list.find_all(5)


def test_delete_node_one_value():
    node_1, node_2, node_3 = create_node(3)
    linked_list = LinkedList()
    linked_list.add_in_tail(node_1)
    linked_list.add_in_tail(node_2)
    linked_list.add_in_tail(node_3)
    linked_list.delete(2)
    assert not linked_list.find_all(2)


def test_delete_node_all_value():
    node_1, node_2, node_3 = create_node(3)
    linked_list = LinkedList()
    node_4 = Node(2)
    linked_list.add_in_tail(node_1)
    linked_list.add_in_tail(node_2)
    linked_list.add_in_tail(node_3)
    linked_list.add_in_tail(node_4)
    linked_list.delete(2, all=True)
    assert not linked_list.find_all(2)


def test_clean_list():
    node_1, node_2, node_3 = create_node(3)
    linked_list = LinkedList()
    linked_list.add_in_tail(node_1)
    linked_list.add_in_tail(node_2)
    linked_list.add_in_tail(node_3)
    linked_list.clean()
    assert not linked_list.head
    assert not linked_list.tail


def test_get_len_list():
    node_1, node_2, node_3 = create_node(3)
    linked_list = LinkedList()
    linked_list.add_in_tail(node_1)
    linked_list.add_in_tail(node_2)
    linked_list.add_in_tail(node_3)
    assert linked_list.len() == 3


def test_delete_tail_element():
    node_1, node_2, node_3 = create_node(3)
    linked_list = LinkedList()
    linked_list.add_in_tail(node_1)
    linked_list.add_in_tail(node_2)
    linked_list.add_in_tail(node_3)
    linked_list.delete(node_3.value)
    assert linked_list.len() == 2


def test_insert_node():
    node_1, node_2, node_3 = create_node(3)
    linked_list = LinkedList()
    node_target = Node(7)
    linked_list.add_in_tail(node_1)
    linked_list.add_in_tail(node_2)
    linked_list.add_in_tail(node_3)
    linked_list.insert(linked_list.head.next, node_target)
    assert linked_list.find(7).next.value == node_3.value
    assert linked_list.find(2).next.value == node_target.value


def test_insert_tail_list():
    node_1, node_2, node_3 = create_node(3)
    linked_list = LinkedList()
    node_target = Node(7)
    linked_list.add_in_tail(node_1)
    linked_list.add_in_tail(node_2)
    linked_list.add_in_tail(node_3)
    linked_list.insert(linked_list.tail, node_target)
    assert linked_list.find(7).next is None
    assert linked_list.find(3).next.value == node_target.value


def test_check_sum_lists():
    node_1, node_2, node_3 = create_node(3)
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    linked_list_1.add_in_tail(node_1)
    linked_list_1.add_in_tail(node_2)
    linked_list_1.add_in_tail(node_3)
    linked_list_2.add_in_tail(node_1)
    linked_list_2.add_in_tail(node_2)
    linked_list_2.add_in_tail(node_3)
    sum_result = sum_linked_lists(linked_list_1, linked_list_2)
    assert sum_result.head.value == 2
    assert sum_result.head.next.value == 4
    assert sum_result.head.next.next.value == 6


def test_check_sum_difference_len():
    node_1, node_2, node_3, node_4, node_5 = create_node(5)
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    linked_list_1.add_in_tail(node_1)
    linked_list_1.add_in_tail(node_2)
    linked_list_1.add_in_tail(node_3)
    linked_list_2.add_in_tail(node_4)
    linked_list_2.add_in_tail(node_5)
    sum_result = sum_linked_lists(linked_list_1, linked_list_2)
    assert not sum_result
