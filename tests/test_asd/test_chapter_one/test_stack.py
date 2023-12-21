import pytest

from asd.chapter_one.stack import Stack, parsing_string


class TestStackEmpty:
    @pytest.fixture
    def stack(self):
        return Stack()

    def test_pop_empty_stack(self, stack):
        assert not stack.pop()

    def test_push_empty_stack(self, stack):
        stack.push(1)
        assert stack.stack[0] == 1
        assert stack.size() == 1

    def test_peek_empty_stack(self, stack):
        assert not stack.peek()

    def test_size_empty_stack(self, stack):
        assert stack.size() == 0


class TestParsingString:
    def test_parsing_string_1(self):
        assert not parsing_string("((())")

    def test_parsing_string_2(self):
        assert not parsing_string("))((")

    def test_parsing_string_3(self):
        assert not parsing_string("())(")

    def test_parsing_string_4(self):
        assert not parsing_string("(()()(()")

    def test_parsing_string_5(self):
        assert parsing_string("(()((())()))")


class TestStackOneElementInStack:
    @pytest.fixture
    def stack(self):
        stack = Stack()
        stack.push(1)
        return stack

    def test_pop_stack(self, stack):
        stack.pop()
        assert stack.size() == 0

    def test_push_stack(self, stack):
        stack.push(2)
        assert stack.stack[0] == 2
        assert stack.size() == 2

    def test_peek_stack(self, stack):
        assert stack.peek() == 1

    def test_size_stack(self, stack):
        assert stack.size() == 1


class TestStackFilledStack:
    @pytest.fixture
    def stack(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        return stack

    def test_pop_stack(self, stack):
        stack.pop()
        assert stack.size() == 3
        assert stack.stack[0] == 3

    def test_push_stack(self, stack):
        stack.push(5)
        assert stack.stack[0] == 5
        assert stack.size() == 5

    def test_peek_stack(self, stack):
        assert stack.peek() == 4

    def test_size_stack(self, stack):
        assert stack.size() == 4
