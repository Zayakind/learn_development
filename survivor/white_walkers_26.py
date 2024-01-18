def search_digit_indexes(value: str) -> list:
    return [i for i in range(len(value)) if value[i].isdigit()]


def search_white_walkers(substring: str) -> int:
    return substring.count('=')


def white_walkers(village: str) -> bool:
    digit_indexes = search_digit_indexes(village)

    if len(digit_indexes) <= 1:
        return False

    count_pairs, count_walkers = 0, 0
    for i in range(len(digit_indexes) - 1):
        if int(village[digit_indexes[i]]) + int(village[digit_indexes[i + 1]]) != 10:
            continue
        count_pairs += 1
        amount_walkers = search_white_walkers(
            village[digit_indexes[i]:digit_indexes[i + 1] + 1]
        )
        if amount_walkers == 3:
            count_walkers += 1
    return count_walkers == count_pairs
