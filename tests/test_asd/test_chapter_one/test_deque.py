import pytest

from asd.chapter_one.deque import Deque, check_palindrome


@pytest.fixture
def deque():
    return Deque()


def test_palindrome():
    letters = 'asdxdsasdxdsa'
    assert check_palindrome(letters) is True


def test_create_empty_deque(deque):
    assert deque.size() == 0


def test_add_head(deque):
    deque.addFront("front")
    assert deque.size() == 1
    assert deque.items[0] == "front"


def test_add_tail(deque):
    deque.addFront("front")
    deque.addTail("tail")
    assert deque.size() == 2
    assert deque.items[-1] == "tail"


def test_add_more_head(deque):
    for letter in "head":
        deque.addFront(letter)
    assert deque.size() == 4
    assert deque.items[0] == "d"


def test_add_more_tail(deque):
    for letter in "tail":
        deque.addTail(letter)
    assert deque.size() == 4
    assert deque.items[-1] == "l"


def test_remove_head(deque):
    for letter in "head":
        deque.addTail(letter)
    deque.removeFront()
    assert deque.size() == 3
    assert deque.items[0] == "e"


def test_remove_tail(deque):
    for letter in "tail":
        deque.addTail(letter)
    deque.removeTail()
    assert deque.size() == 3
    assert deque.items[-1] == "i"


def test_remove_all(deque):
    for letter in "tail":
        deque.addTail(letter)
    for _ in range(deque.size()):
        deque.removeTail()
    assert deque.size() == 0


def test_add_and_check_in_deque(deque):
    for letter in "tail":
        deque.addTail(letter)
    assert "i" in deque.items


def test_remove_and_check_not_in_deque(deque):
    for letter in "tail":
        deque.addTail(letter)
    deque.removeTail()
    assert "l" not in deque.items
