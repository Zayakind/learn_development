from eight_algoritms.army_communication_matrix import army_communication_matrix


def test_1():
    mtrx = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert army_communication_matrix(3, mtrx) == "1 1 2"


def test_2():
    mtrx = [
        [1, 9, 2, 3],
        [4, 8, 5, 6],
        [0, 7, 1, 2],
        [0, 0, 0, 0]
    ]
    assert army_communication_matrix(4, mtrx) == "1 0 3"
