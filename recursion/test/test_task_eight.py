import os

from recursion.task_eight import find_files


def test_1():
    print(os.getcwd())
    temp = find_files("..")
    for tm in temp:
        print(tm)
