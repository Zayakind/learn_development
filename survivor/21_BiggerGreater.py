from itertools import *


def BiggerGreater(string: str) -> str:
    sorted_unique_options = sorted(set(map(''.join, permutations(string))))
    if len(sorted_unique_options) <= 1 or sorted_unique_options[-1] == string:
        return ""
    index = sorted_unique_options.index(string)
    return sorted_unique_options[index+1]
