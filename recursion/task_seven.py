def search_recursive(numbers: list, first_max: float | int, second_max: float | int, count: int) -> int:
    if count == len(numbers):
        return second_max

    next_count = count + 1

    if numbers[count] > second_max:
        first_max = first_max
        second_max = numbers[count]

    if numbers[count] > first_max:
        first_max, second_max = numbers[count], first_max

    return search_recursive(numbers, first_max, second_max, next_count)


def find_second_max(data: list) -> int:
    first_max, second_max = data[0], data[1]
    if second_max > first_max:
        first_max, second_max = second_max, first_max
    return search_recursive(data, first_max, second_max, 2)
