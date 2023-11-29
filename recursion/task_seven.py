
def tail_recursive(numbers: list, first_max: float | int, second_max: float | int) -> int:
    if not numbers:
        return second_max
    temp = numbers.pop(0)
    if temp >= first_max:
        return tail_recursive(numbers, temp, first_max)
    if temp > second_max:
        return tail_recursive(numbers, first_max, temp)
    return tail_recursive(numbers, first_max, second_max)


def find_second_max(data: list) -> int:
    first_max = float('-inf')
    second_max = float('-inf')
    return tail_recursive(data, first_max, second_max)
