import os

from recursion.task_eight import find_files


def test_1():
    print(os.getcwd())
    print(find_files("."))
