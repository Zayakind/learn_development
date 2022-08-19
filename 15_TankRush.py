
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
                break

    return check


def entry_map(card: list[list[int]], example: list[list[int]]) -> bool:

    check = []
    flag = False

    for index_example, value_example in enumerate(example):
        for index_card, value_card in enumerate(card):
            if str(value_example).strip('[]') in str(value_card).strip('[]'):
                check.append(value_example) if value_example not in check else None

    if check and check_valid(card, example):
        flag = True

    return flag


def TankRush(line_1: int, column_1: int, data_1: str, line_2: int, column_2: int, data_2: str) -> bool:
    first_map = create_map(line_1, column_1, data_1)
    second_map = create_map(line_2, column_2, data_2)
    return entry_map(first_map, second_map)


print(TankRush(15,15,'900934352126360 119214144058652 979486082875698 322436531185165 887105930987956 232802644488782 302771989566798 073573207654780 311755785362806 909007939272309 395094805516080 562910805349811 993854324744973 768703404219199 630625270887199',2,2,'99 99'))

# 321
# 694  x, y =  x + 1, y
# 798

# 69
# 98