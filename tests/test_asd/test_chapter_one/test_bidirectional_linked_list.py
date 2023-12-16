from asd.chapter_one.bidirectional_linked_list import LinkedList2, Node


def create_node(count: int) -> list[Node]:
    return [Node(i+1) for i in range(count)]


def test_find_empty_list():
    linked_list = LinkedList2()
    assert not linked_list.find(2)


def test_find_one_elem_in_list():
    linked_list = LinkedList2()
    node = Node(2)
    linked_list.add_in_tail(node)
    assert linked_list.find(2).value == node.value


def test_find_more_object_in_list():
    linked_list = LinkedList2()
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    linked_list.add_in_tail(node_1)
    linked_list.add_in_tail(node_2)
    linked_list.add_in_tail(node_3)
    linked_list.add_in_tail(node_4)
    assert linked_list.find(2).value == node_2.value


def test_find_all_empty_list():
    linked_list = LinkedList2()
    assert not linked_list.find(2)


def test_find_all_one_elem_in_list():
    linked_list = LinkedList2()
    node = Node(2)
    linked_list.add_in_tail(node)
    assert linked_list.find(2) in [node]


def test_find_all_more_object_in_list():
    linked_list = LinkedList2()
    node_1, node_2, node_3, node_5 = create_node(4)
    node_4 = Node(2)
    linked_list.add_in_tail(node_1)
    linked_list.add_in_tail(node_2)
    linked_list.add_in_tail(node_3)
    linked_list.add_in_tail(node_4)
    linked_list.add_in_tail(node_5)
    assert linked_list.find(2) in [node_2, node_5]


def test_delete_first_elem():
    linked_list = LinkedList2()
    node_1, node_2 = create_node(2)
    linked_list.add_in_tail(node_1)
    linked_list.add_in_tail(node_2)
    linked_list.delete(node_1.value)
    assert linked_list.head.value == node_2.value
    assert linked_list.tail.value == node_2.value
    assert linked_list.head.next is None
    assert linked_list.head.prev is None


def test_delete_tail_elem():
    linked_list = LinkedList2()
    node_1, node_2 = create_node(2)
    linked_list.add_in_tail(node_1)
    linked_list.add_in_tail(node_2)
    linked_list.delete(node_2.value)
    assert linked_list.head.value == node_1.value
    assert linked_list.tail.value == node_1.value
    assert linked_list.head.next is None
    assert linked_list.head.prev is None


def test_delete_elem():
    linked_list = LinkedList2()
    node_1, node_2, node_3 = create_node(3)
    linked_list.add_in_tail(node_1)
    linked_list.add_in_tail(node_2)
    linked_list.add_in_tail(node_3)
    linked_list.delete(node_2.value)
    assert linked_list.head.value == node_1.value
    assert linked_list.tail.value == node_3.value


def test_delete_empty_list():
    linked_list = LinkedList2()
    assert linked_list.delete(3) is None


def test_delete_several_elem():
    linked_list = LinkedList2()
    node_1, node_2, node_3, node_5 = create_node(4)
    node_4 = Node(2)
    linked_list.add_in_tail(node_1)
    linked_list.add_in_tail(node_2)
    linked_list.add_in_tail(node_3)
    linked_list.add_in_tail(node_4)
    linked_list.add_in_tail(node_5)
    linked_list.delete(node_2.value, all=True)
    assert linked_list.head.value == node_1.value
    assert linked_list.tail.value == node_5.value
    assert linked_list.find_all(2) == []


def test_insert_to_empty_list():
    linked_list = LinkedList2()
    node = Node(1)
    linked_list.insert(None, node)
    assert linked_list.head.value == node.value
    assert linked_list.tail.value == node.value
    assert linked_list.head.next is None
    assert linked_list.tail.prev is None
    assert linked_list.tail == linked_list.head



def test_insert_filled_list():
    linked_list = LinkedList2()
    node_1, node_2, node_3, node_4 = create_node(4)
    node_5 = Node(5)
    linked_list.add_in_tail(node_1)
    linked_list.add_in_tail(node_2)
    linked_list.add_in_tail(node_3)
    linked_list.add_in_tail(node_4)
    linked_list.insert(None, node_5)
    find_node = linked_list.find(5)
    assert find_node.prev is node_4
    assert find_node.next is None
    assert linked_list.tail is node_5


def test_insert_after_node():
    linked_list = LinkedList2()
    node_1, node_2 = create_node(2)
    node_3 = Node(3)
    linked_list.add_in_tail(node_1)
    linked_list.add_in_tail(node_2)
    linked_list.insert(node_1, node_3)
    assert linked_list.head is node_1
    assert linked_list.tail is node_2
    find_node = linked_list.find(3)
    assert find_node.prev is node_1
    assert find_node.next is node_2


def test_insert_after_node_tail_list():
    linked_list = LinkedList2()
    node_1 = create_node(1)[0]
    node_3 = Node(3)
    linked_list.add_in_tail(node_1)
    linked_list.insert(node_1, node_3)
    assert linked_list.head is node_1
    assert linked_list.tail is node_3
    find_node = linked_list.find(3)
    assert find_node.prev is node_1
    assert find_node.next is None


def test_add_head_empty_list():
    linked_list = LinkedList2()
    node_1 = create_node(1)[0]
    linked_list.add_in_head(node_1)
    assert linked_list.head is node_1
    assert linked_list.tail is node_1
    assert node_1.next is None
    assert node_1.prev is None


def test_add_head_filled_list():
    linked_list = LinkedList2()
    node_1, node_2 = create_node(2)
    node_3 = Node(3)
    linked_list.add_in_tail(node_1)
    linked_list.add_in_tail(node_2)
    linked_list.add_in_head(node_3)
    assert linked_list.head is node_3
    assert node_3.next is node_1
    assert node_3.prev is None
    assert node_1.prev is node_3


def test_get_len():
    linked_list = LinkedList2()
    node_1, node_2 = create_node(2)
    node_3 = Node(3)
    linked_list.add_in_tail(node_1)
    linked_list.add_in_tail(node_2)
    assert linked_list.len() == 2
    linked_list.add_in_head(node_3)
    assert linked_list.len() == 3


def test_get_len_empty_list():
    linked_list = LinkedList2()
    assert linked_list.len() == 0
