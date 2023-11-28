import random

from ..task_three import calculating_len


def test_1():
    data = [1 for _ in range(50)]
    length_data = len(data)
    assert calculating_len(data) == length_data


def test_2():
    data = []
    assert calculating_len(data) == 0
