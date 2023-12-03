from eight_algoritms.digital_rain import digital_rain


def test_1():
    assert digital_rain("1111000") == "111000"


def test_2():
    assert digital_rain("11101000") == "11101000"


def test_3():
    assert digital_rain("011111110") == "10"


def test_4():
    assert digital_rain("11111111") == ""
