def matrix(n: int, m: int, matrix: list) -> list[int]:
    result = []
    start_row, end_row = 0, m - 1
    start_col, end_col = 0, n - 1

    while start_row <= end_row and start_col <= end_col:
        for i in range(start_col, end_col + 1):
            result.append(matrix[start_row][i])
        start_row += 1

        for i in range(start_row, end_row + 1):
            result.append(matrix[i][end_col])
        end_col -= 1

        if start_row <= end_row:
            for i in range(end_col, start_col - 1, -1):
                result.append(matrix[end_row][i])
            end_row -= 1

        if start_col <= end_col:
            for i in range(end_row, start_row - 1, -1):
                result.append(matrix[i][start_col])
            start_col += 1

    return result
