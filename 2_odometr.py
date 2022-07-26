def odometr(oksana: list[int]) -> int:
    result = 0

    for hour in range(1, len(oksana), 2):
        if hour != 1:
            summ_hour = oksana[hour-1] * (oksana[hour] - oksana[hour-2])
        else:
            summ_hour = oksana[hour-1] * oksana[hour]
        result += summ_hour
    return result

