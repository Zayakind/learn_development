
def changed_data(data: list[int], index: int) -> list[int]:

    temp = [data[index - 2], data[index - 1], data[index]]
    while temp[0] != min(temp):
        data.insert(index-2, data.pop(index - 1))
        data.insert(index-1, data.pop(index))
        temp = [data[index - 2], data[index - 1], data[index]]

    return data


def MisterRobot(N: int, data: list[int]) -> bool:

    check = False
    sorted_data = data[:]
    sorted_data.sort()

    for num in range(N - 1, -1, -1):
        if data[num] == N:
            N -= 1
            continue
        changed_data(data, num)
        N -= 1

    if sorted_data == data:
        check = True

    return check