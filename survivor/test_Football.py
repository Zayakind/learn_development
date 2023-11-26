from Football_27 import Football


def test_1():
    assert Football([1, 3, 2], 3)


def test_2():
    assert Football([1, 7, 5, 3, 9], 5)


def test_3():
    assert Football([3, 2, 1], 3)


def test_4():
    assert Football([1, 4, 3, 2, 5], 5)


def test_5():
    assert not Football([9, 5, 3, 7, 1], 5)


def test_6():
    assert not Football([1, 2, 3], 3)
