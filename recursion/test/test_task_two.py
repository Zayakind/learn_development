from ..task_two import summ


def test_1():
    assert summ(11111) == 5


def test_2():
    assert summ(22222) == 10


def test_3():
    assert summ(135) == 9


def test_4():
    assert summ(546) == 15
