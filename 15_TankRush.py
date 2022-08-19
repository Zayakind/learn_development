
def create_map(row: int, column: int, data: str) -> list[list[int]]:

    result = [[] * column] * row
    data = data.split(' ')

    for index, row_iter in enumerate(result):
        result[index] = list(int(x) for x in data[index])

    return result


def check_valid(maps: list[list[int]], example: list[list[int]]) -> bool:

    check = False
    search = example[0][0]

    for index_row, row in enumerate(maps):
        for index_col, value_col in enumerate(row):
            if row != maps[-1] and value_col == search and maps[index_row + 1][index_col] == example[1][0] and maps[index_row + 1][index_col + 1] == example[1][1]:
                check = True

    return check


def entry_map(card: list[list[int]], example: list[list[int]]) -> bool:

    check = []
    flag = False

    for index_example, value_example in enumerate(example):
        for index_card, value_card in enumerate(card):
            if str(value_example).strip('[]') in str(value_card).strip('[]'):
                check.append(value_example) if value_example not in check else None

    if check == example and check_valid(card, example):
        flag = True

    return flag


def TankRush(line_1: int, column_1: int, data_1: str, line_2: int, column_2: int, data_2: str) -> bool:
    first_map = create_map(line_1, column_1, data_1)
    second_map = create_map(line_2, column_2, data_2)
    return entry_map(first_map, second_map)
