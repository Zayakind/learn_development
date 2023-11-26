from copy import deepcopy


def odometer(oksana: list[int]) -> int:
    result, last_time = 0, 0
    for speed, time in zip(oksana[0::2], oksana[1::2]):
        result += speed * (time - last_time)
        last_time = time
    return result


def squirrel(n: int) -> int:
    if n == 1 or n == 0:
        return 1
    factorial = 1
    for i in range(2, n+1):
        factorial *= i
    while factorial > 10:
        factorial = factorial // 10
    return factorial


def SynchronizingTables(N: int, ids: list[int], salary: list[int]) -> list[int]:
    sort_ids, sort_salary = sorted(ids), sorted(salary)
    table_ids_and_salary = dict(zip(sort_ids, sort_salary))
    return [table_ids_and_salary[worker] for worker in ids]


def capture_success(square: list[list[int]]) -> bool:
    for n in square:
        for m in n:
            if m == 0:
                return False
    return True


def started_day(L: int, first_started: list[int], square: list[list[int]]) -> None:
    temp = 0
    for _ in range(L):
        n, m = first_started[temp] - 1, first_started[temp + 1] - 1
        square[n][m] += 1
        temp += 2


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


def seizure_of_territory(square: list[list[int]], day_war: int) -> int:
    double = deepcopy(square)

    for index_n, value_n in enumerate(double):
        for index_m, value_m in enumerate(value_n):
            if value_m > 0:
                capture_area(square, index_n, index_m)
    day_war += 1
    if capture_success(square):
        return day_war
    return seizure_of_territory(square, day_war)


def ConquestCampaign(N: int, M: int, L: int, battalion: list) -> int:
    square = [[0] * M for _ in range(N)]
    day_war = 1
    started_day(L, battalion, square)
    if capture_success(square):
        return day_war
    day_war = seizure_of_territory(square, day_war)
    return day_war


def SumOfThe(N: int, data: list[int]) -> int:
    result = [sym for sym in data if sum(data) - sym == sym]
    return result[0]
