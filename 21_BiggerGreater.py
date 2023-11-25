from itertools import *


def BiggerGreater(string: str) -> str:
    sort_options = sorted(set(map(''.join, permutations(string))))
    if len(sort_options) <= 1 or sort_options[-1] == string:
        return ""
    index = sort_options.index(string)
    return sort_options[index+1]
