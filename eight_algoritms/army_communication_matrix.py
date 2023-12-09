def army_communication_matrix(n: int, matrix: list) -> str:
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # заполнение матрицы dp
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = matrix[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

    max_sum = float('-inf')
    max_coords = (0, 0)
    max_size = 0

    # поиск максимальной суммы и сохранение координат и размера подматрицы
    for m in range(2, n):
        for i in range(n - m + 1):
            for j in range(n - m + 1):
                sum_m = dp[i + m][j + m] - dp[i + m][j] - dp[i][j + m] + dp[i][j]
                if sum_m > max_sum:
                    max_sum = sum_m
                    max_coords = (i, j)
                    max_size = m

    return f"{max_coords[1]} {max_coords[0]} {max_size}"
