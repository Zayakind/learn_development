from asd.chapter_one.linked_list import Node, LinkedList, sum_linked_lists

import pytest


def create_node(count: int) -> list[Node]:
    return [Node(i+1) for i in range(count)]


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


def test_checking_the_initial_length_of_the_list():
    linked_list = LinkedList()
    assert linked_list.len() == 0


def test_checking_the_initial_state_of_pointers_to_the_first_and_last_nodes():
    linked_list = LinkedList()
    assert linked_list.head is None
    assert linked_list.tail is None


def test_checking_adding_to_an_empty_list():
    linked_list = LinkedList()
    node = Node(1)
    linked_list.add_in_tail(node)
    assert linked_list.head is node
    assert linked_list.tail is node


def test_checking_for_adding_to_a_non_empty_list():
    linked_list = LinkedList()
    node_1 = Node(1)
    node_2 = Node(2)
    linked_list.add_in_tail(node_1)
    assert linked_list.head is node_1
    assert linked_list.tail is node_1

    linked_list.add_in_tail(node_2)
    assert linked_list.tail is node_2
    assert linked_list.head is node_1


def test_check_for_changes_in_list_length():
    node_1, node_2 = create_node(2)
    linked_list = LinkedList()
    linked_list.add_in_tail(node_1)
    linked_list.add_in_tail(node_2)
    assert linked_list.len() == 2


def test_get_len_after_delete():
    node_1, node_2 = create_node(2)
    linked_list = LinkedList()
    linked_list.add_in_tail(node_1)
    linked_list.add_in_tail(node_2)
    linked_list.delete(2)
    assert linked_list.len() == 1


def test_get_len_after_clean_list():
    node_1, node_2 = create_node(2)
    linked_list = LinkedList()
    linked_list.add_in_tail(node_1)
    linked_list.add_in_tail(node_2)
    linked_list.clean()
    assert linked_list.len() == 0


def test_checking_the_console_output_of_a_non_empty_list(capsys):
    node_1, node_2, node_3 = create_node(3)
    linked_list = LinkedList()
    linked_list.add_in_tail(node_1)
    linked_list.add_in_tail(node_2)
    linked_list.add_in_tail(node_3)
    linked_list.print_all_nodes()
    assert capsys.readouterr().out.replace("\n", " ").strip() == "1 2 3"


def test_checking_the_output_of_an_empty_list_to_the_console(capsys):
    linked_list = LinkedList()
    linked_list.print_all_nodes()
    assert capsys.readouterr().out.replace("\n", " ").strip() == ""


def test_search_for_an_existing_node():
    node_1, node_2, node_3 = create_node(3)
    linked_list = LinkedList()
    linked_list.add_in_tail(node_1)
    linked_list.add_in_tail(node_2)
    linked_list.add_in_tail(node_3)
    assert linked_list.find(2) is node_2


def test_search_for_a_non_existing_node():
    linked_list = LinkedList()
    assert linked_list.find(2) is None


def test_search_all_existing_nodes_by_value():
    node_1, node_2, node_3 = create_node(3)
    node_4 = Node(4)
    node_5 = Node(2)
    linked_list = LinkedList()
    linked_list.add_in_tail(node_1)
    linked_list.add_in_tail(node_2)
    linked_list.add_in_tail(node_3)
    linked_list.add_in_tail(node_4)
    linked_list.add_in_tail(node_5)
    assert linked_list.find_all(2) == [node_2, node_5]


def test_deleting_one_existing_node():
    node_1 = create_node(1)[0]
    linked_list = LinkedList()
    linked_list.add_in_tail(node_1)
    linked_list.delete(1)
    assert linked_list.find(1) is None
    assert linked_list.len() == 0
    assert linked_list.head is None
    assert linked_list.tail is None


def test_delete_all_nodes_with_a_given_value():
    node_1 = Node(1)
    node_2 = Node(1)
    node_3 = Node(1)
    node_4 = Node(1)
    linked_list = LinkedList()
    linked_list.add_in_tail(node_1)
    linked_list.add_in_tail(node_2)
    linked_list.add_in_tail(node_3)
    linked_list.add_in_tail(node_4)
    linked_list.delete(1, True)
    assert linked_list.find(1) is None
    assert linked_list.len() == 0
    assert linked_list.head is None
    assert linked_list.tail is None


def test_checking_that_the_list_is_completely_cleared():
    node_1 = create_node(1)[0]
    linked_list = LinkedList()
    linked_list.add_in_tail(node_1)
    linked_list.clean()
    assert linked_list.head is None and linked_list.tail is None


def test_checking_the_correctness_of_changing_the_length_of_the_list():
    node_1 = create_node(1)[0]
    linked_list = LinkedList()
    linked_list.add_in_tail(node_1)
    linked_list.clean()
    assert linked_list.len() == 0


def test_checking_in_tail_an_empty_list():
    node_1 = create_node(1)[0]
    linked_list = LinkedList()
    linked_list.add_in_tail(node_1)
    assert linked_list.head is node_1 and linked_list.len() == 1


def test_checking_insertion_into_an_empty_list():
    node_1 = create_node(1)[0]
    linked_list = LinkedList()
    linked_list.insert(new_node=node_1)
    assert linked_list.head is node_1 and linked_list.len() == 1
    assert linked_list.tail is node_1


def test_checking_for_insertion_into_a_non_empty_list():
    node_1 = create_node(1)[0]
    linked_list = LinkedList()
    linked_list.add_in_tail(node_1)
    node_2 = Node(2)
    linked_list.add_in_tail(node_2)
    assert linked_list.head is node_1 and linked_list.len() == 2 and linked_list.tail is node_2
