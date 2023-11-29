
def search_recursive(numbers: list, first_max: float | int, second_max: float | int, count: int) -> int:
    if count == len(numbers):
        return second_max
    if numbers[count] > first_max > second_max:
        return search_recursive(numbers, numbers[count], first_max, count + 1)
    if numbers[count] > first_max and first_max < second_max:
        return search_recursive(numbers, numbers[count], second_max, count + 1)
    if numbers[count] > second_max:
        return search_recursive(numbers, first_max, numbers[count], count + 1)
    return search_recursive(numbers, first_max, second_max, count + 1)


def find_second_max(data: list) -> int:
    first_max = data[0]
    second_max = data[1]
    return search_recursive(data, first_max, second_max, 2)
