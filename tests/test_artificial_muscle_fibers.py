from eight_algoritms.artificial_muscle_fibers import artificial_muscle_fibers


def test_1():
    assert artificial_muscle_fibers([1, 2, 3, 4, 5]) == 0


def test_2():
    assert artificial_muscle_fibers([1, 2, 3, 2, 1]) == 2


def test_3():
    assert artificial_muscle_fibers([1, 2, 3, 2, 1, 2, 4, 2, 1]) == 2
