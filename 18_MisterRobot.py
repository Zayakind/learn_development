from copy import copy


def one_operation(data: list[int], number: int, index: int) -> list[int]:

    while data[index] != number:
        changed_data(data, number)

    return data


def changed_data(data: list[int], number: int) -> list[int]:

    index = data.index(number)
    temp = [data[index - 2], data[index - 1], data[index]]
    while temp[0] != number:
        data.insert(index-2, data.pop(index - 1))
        data.insert(index-1, data.pop(index))
        temp = [data[index - 2], data[index - 1], data[index]]

    return data


def MisterRobot(N: int, data: list[int]) -> bool:

    check = False
    check_number = 1
    sort_data = copy(data)
    sort_data.sort()

    for index, value in enumerate(data):
        if data == sort_data:
            check = True
            break
        if value != check_number:
            one_operation(data, check_number, index)

        check_number += 1

    return check
