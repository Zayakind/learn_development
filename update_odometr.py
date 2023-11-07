def odometer(oksana: list[int]) -> int:
    result, last_time = 0, 0
    for speed, time in zip(oksana[0::2], oksana[1::2]):
        result += speed * (time - last_time)
        last_time = time
    return result

