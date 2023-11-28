from recursion.task_four import checking_palindrom


def test_1():
    assert checking_palindrom("шабаш")


def test_2():
    assert checking_palindrom("уху")


def test_3():
    assert checking_palindrom("амма")


def test_4():
    assert not checking_palindrom("аммаa")
