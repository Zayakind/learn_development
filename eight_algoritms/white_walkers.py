def search_digit_indexes(value: str) -> list:
    return list(map(lambda x: x[0], filter(lambda x: x[1].isdigit(), enumerate(value))))


def search_white_walkers(substring: str) -> int:
    count_letter = 0
    for letter in substring:
        if letter == '=':
            count_letter += 1
    return count_letter


def white_walkers(village: str) -> bool:
    digit_indexes = search_digit_indexes(village)

    if len(digit_indexes) <= 1:
        return False

    count_pairs, count_walkers = 0, 0
    for i, j in zip(digit_indexes, digit_indexes[1:]):
        if int(village[i]) + int(village[j]) != 10:
            continue
        count_pairs += 1
        amount_white_walkers = search_white_walkers(village[i:j + 1])
        if amount_white_walkers == 3:
            count_walkers += 1
    return count_walkers == count_pairs
