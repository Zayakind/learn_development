from eight_algoritms.eec_help import EEC_help

def test_1():
    assert EEC_help([1,2,3], [1,2,3,4]) == False


def test_2():
    assert EEC_help([1,2,3], [1,2,3]) == True


def test_3():
    assert EEC_help([1,3,2], [1,2,3]) == True


def test_4():
    assert EEC_help([1,3,2,3], [1,2,2,3]) == False


def test_5():
    assert EEC_help([1,1], [1,1]) == True
