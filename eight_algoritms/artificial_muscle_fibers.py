def artificial_muscle_fibers(array: list[int]) -> int:
    buffer = {}
    duplicates = 0
    for num in array:
        if buffer.get(num):
            buffer[num] += 1
            continue
        buffer[num] = 1
    for k, v in buffer.items():
        if v > 1:
            duplicates += 1
    return duplicates
