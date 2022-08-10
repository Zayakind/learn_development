
def UFO(N: int, data: list[int], octal: bool) -> list[int]:

    if octal:
        result = [int(str(numb), 8) for numb in data]
        return result

    result = [int(str(numb), 16) for numb in data]
    return result
