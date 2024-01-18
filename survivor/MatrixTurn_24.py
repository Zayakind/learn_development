def one_rotation(matrix: list[str], row: int, line: int) -> None:
    top, bottom = 0, row - 1
    left, right = 0, line - 1

    amount_rotated = int(row / 2)
    for _ in range(amount_rotated):
        top_left = matrix[left][left]

        for i in range(top, bottom):
            matrix[i][left] = matrix[i + 1][left]

        for j in range(left, right):
            matrix[bottom][j] = matrix[bottom][j + 1]

        for i in range(bottom - 1, top - 1, -1):
            matrix[i + 1][right] = matrix[i][right]

        for j in range(right - 1, left, -1):
            matrix[top][j + 1] = matrix[top][j]

        matrix[left][left + 1] = top_left

        if left == line - 1 or top == row - 1:
            break
        top, bottom = top + 1, bottom - 1
        left, right = left + 1, right - 1


def MatrixTurn(matrix: list[str], m_row: int, n_line: int, t_count: int) -> None:
    for i, row in enumerate(matrix):
        matrix[i] = list(row)

    for _ in range(t_count):
        one_rotation(matrix, m_row, n_line)

    for i, row in enumerate(matrix):
        matrix[i] = ''.join(row)
