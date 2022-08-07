
def format_result(data: str) -> str:

    data = data[::-1]

    while True:
        if data[0] == "0" and len(data) > 1:
            data = data[1:]
        else:
            break

    return data


def search_index(listed: list[str], index: int) -> int:

    while True:
        if listed[index] == 0:
            index += 1
        else:
            break

    return index


def BigMinus(s1: str, s2: str) -> str:

    reduced = list(s1[::-1])
    deductible = list(s2[::-1])
    result = ''

    if len(s1) < len(s2):
        reduced = list(s2[::-1])
        deductible = list(s1[::-1])

    if len(reduced) == 1:
        reduced = max(int(s1), int(s2))
        deductible = min(int(s1), int(s2))
        return f"{reduced - deductible}"

    for index, value in enumerate(reduced):
        if len(deductible) - 1 >= index:
            if int(value) < int(deductible[index]):
                index_next = search_index(reduced, index + 1)
                reduced[index_next] = int(reduced[index_next]) - 1
                value = int(value) + 10
            result += str(int(value) - int(deductible[index]))
            continue
        result += str(value)

    result = format_result(result)

    return result


print(BigMinus('1234567890', '1234567890'))
