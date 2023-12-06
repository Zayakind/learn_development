from eight_algoritms.trc_sort import TRC_sort


def test_1():
    assert TRC_sort([2, 1, 0]) == [0, 1, 2]


def test_2():
    assert TRC_sort([0, 1, 2, 1, 0, 2]) == [0, 0, 1, 1, 2, 2]


def test_3():
    assert TRC_sort([0, 1, 2]) == [0, 1, 2]


def test_4():
    assert TRC_sort([2]) == [2]
