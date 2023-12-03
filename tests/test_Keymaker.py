from survivor.Keymaker_28 import Keymaker


def test_1():
    assert Keymaker(5) == '10010'


def test_2():
    assert Keymaker(10) == '1001000010'
