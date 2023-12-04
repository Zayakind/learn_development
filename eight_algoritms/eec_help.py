def EEC_help(array_one: list[int], array_two: list[int]) -> bool:
    if len(array_one) != len(array_two):
        return False
    for one, two in zip(sorted(array_one), sorted(array_two)):
        if one != two:
            return False
    return True
