from eight_algoritms.massdriver import massdriver


def test_1():
    assert massdriver([1, 2, 3, 1, 2, 3, 4]) == 0


def test_2():
    assert massdriver([1, 2, 3, 4, 3, 4, 2]) == 1


def test_3():
    assert massdriver([1, 2, 3, 4, 5, 6, 7]) == -1
