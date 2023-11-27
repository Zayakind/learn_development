from ..task_one import exponentiation


def test_1():
    assert exponentiation(2, 3) == 8


def test_2():
    assert exponentiation(2, 13) == 8192


def test_3():
    assert exponentiation(5, -2) == 0.04


def test_4():
    assert exponentiation(0, 0) == 1


def test_5():
    assert exponentiation(-3, -3) == -0.037037037037037035
