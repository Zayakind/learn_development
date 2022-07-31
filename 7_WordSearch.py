
def pars_string(result: list, data_str: str, lens: int) -> list[str]:

    word = ''

    for index, letter in enumerate(data_str):
        word += letter
        if letter == ' ' or letter == data_str[-1]:
            if data_str[index + 1:].find(' ') > lens - len(word) or data_str[index + 1:].find(' ') == -1:
                result.append(word.strip())
                word = ''

    return result


def checker_subs(subs: str, data: list[str]) -> list[int]:
    result = []
    for word in data:
        if subs in word.split(' '):
            result.append(1)
            continue
        result.append(0)

    return result


def WordSearch(lens: int, s: str, subs: str) -> list[int]:
    result = []
    result = pars_string(result, s, lens)

    return checker_subs(subs, result)
