def odometer(oksana: list[int]) -> int:
    sammary_km = 0

    for hour in range(1, len(oksana), 2):
        if hour != 1:
            summ_hour = oksana[hour-1] * (oksana[hour] - oksana[hour-2])
        else:
            summ_hour = oksana[hour-1] * oksana[hour]
        sammary_km += summ_hour
    return sammary_km
