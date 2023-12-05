def EEC_help(array_one: list[int], array_two: list[int]) -> bool:
    if len(array_one) != len(array_two):
        return False

    counts = {}
    for num in array_one:
        counts[num] = counts.get(num, 0) + 1

    for num in array_two:
        if num not in counts or counts[num] == 0:
            return False
        counts[num] -= 1

    return True
