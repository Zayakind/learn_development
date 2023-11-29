from recursion.task_seven import find_second_max


def test_1():
    assert find_second_max([2, 5, 4, 3, 5]) == 5


def test_2():
    assert find_second_max([2, 3, 5, 4]) == 4


def test_3():
    assert find_second_max([-1, -5, -2, -4]) == -2
