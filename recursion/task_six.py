def print_even_indexes(data: list, point: int = None):
    if not point:
        point = 0
    if point >= len(data):
        return
    print(data[point])
    print_even_indexes(data, point + 2)
