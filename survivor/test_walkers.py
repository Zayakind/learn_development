# from white_walkers_26 import white_walkers
from eight_algoritms.white_walkers import white_walkers


def test_1():
    assert white_walkers("axxb6===4xaf5===eee5")


def test_2():
    assert not white_walkers("5==ooooooo=5=5")


def test_3():
    assert white_walkers("abc=7==hdjs=3gg1=======5")


def test_4():
    assert not white_walkers("aaS=8")


def test_5():
    assert white_walkers("9===1===9===1===9")
