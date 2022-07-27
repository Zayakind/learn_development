from copy import deepcopy


def generated_square(n: int, m: int) -> list[list]:

    return [[0] * m for _ in range(n)]


def capture_area(square: list[list], index_n: int, index_m: int) -> list[list]:

    if index_n > 0 and 0 <= index_m <= (len(square[0]) - 1):
        square[index_n - 1][index_m] = 1

    if index_n < (len(square) - 1) and 0 <= index_m <= (len(square[0]) - 1):
        square[index_n + 1][index_m] = 1

    if 0 < index_m and 0 <= index_n <= (len(square) - 1):
        square[index_n][index_m - 1] = 1

    if index_m < (len(square[0]) - 1) and 0 <= index_n <= (len(square) - 1):
        square[index_n][index_m + 1] = 1

    return square


def check_square(square: list[list]) -> bool:

    check = True

    for index_n, value_n in enumerate(square):
        for index_m, value_m in enumerate(value_n):
            if value_m == 0:
                check = False

    return check


def detour_square(square: list[list]) -> tuple[list[list], bool]:

    double = deepcopy(square)

    for index_n, value_n in enumerate(double):
        for index_m, value_m in enumerate(value_n):
            if value_m == 1:
                capture_area(square, index_n, index_m)

    return square, check_square(square)


def started_point(L: int, battalion: list, square: list[list]) -> list[list]:

    for i in range(0, L+1, 2):
        x, y = battalion[i] - 1, battalion[i+1] - 1
        square[x][y] = 1

    return square


def ConquestCampaign(N: int, M: int, L: int, battalion: list) -> int:

    day = 1
    maps = generated_square(N, M)
    started_point(L, battalion, maps)

    while True:
        day += 1
        maps, status = detour_square(maps)
        print(maps)
        if status:
            break

    return day
