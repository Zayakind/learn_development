from SherlockValidString_22 import *


def test_1():
    assert SherlockValidString("xyz")


def test_2():
    assert SherlockValidString("xyzaa")


def test_3():
    assert SherlockValidString("xxyyz")


def test_4():
    assert SherlockValidString("xyzzz") == False


def test_5():
    assert SherlockValidString("xxyyza") == False


def test_6():
    assert SherlockValidString("xxyyzabc") == False


def test_7():
    assert SherlockValidString("xxyyy")


def test_8():
    assert SherlockValidString("xxxyy") == False


def test_8():
    assert SherlockValidString("xyxyzazaz")
