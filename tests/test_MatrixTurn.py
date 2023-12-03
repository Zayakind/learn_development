from survivor.MatrixTurn_24 import MatrixTurn


def test_1():
    matrix = ["123456", "234567", "345678", "456789"]
    result = ["212345", "343456", "456767", "567898"]
    MatrixTurn(
        matrix=matrix,
        m_row=4,
        n_line=6,
        t_count=1,
    )
    for mtrx, rslt in zip(matrix, result):
        assert mtrx == rslt
